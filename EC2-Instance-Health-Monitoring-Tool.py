import boto3
import smtplib
from datetime import datetime, timedelta

# AWS Clients
ec2 = boto3.client('ec2')
cloudwatch = boto3.client('cloudwatch')

# Email Configuration
EMAIL_SENDER = "guruprasad9450@gmail.com"
EMAIL_RECEIVER = "guruprasadbhat37@gmail.com"
EMAIL_PASSWORD = "your_app_password"  # Use App Password if using Gmail
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# Threshold
CPU_THRESHOLD = 70.0

def send_email(instance_id, cpu_usage):
    subject = f"High CPU Alert: {instance_id}"
    body = f"CPU usage for instance {instance_id} is {cpu_usage:.2f}%"
    message = f"Subject: {subject}\n\n{body}"

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, message)

def check_instance_health():
    instances = ec2.describe_instances()
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            state = instance['State']['Name']
            
            if state == 'running':
                metric = cloudwatch.get_metric_statistics(
                    Namespace='AWS/EC2',
                    MetricName='CPUUtilization',
                    Dimensions=[{'Name': 'InstanceId', 'Value': instance_id}],
                    StartTime=datetime.utcnow() - timedelta(minutes=10),
                    EndTime=datetime.utcnow(),
                    Period=300,
                    Statistics=['Average']
                )

                datapoints = metric['Datapoints']
                if datapoints:
                    avg_cpu = datapoints[0]['Average']
                    print(f"Instance {instance_id} - CPU: {avg_cpu:.2f}%")
                    if avg_cpu > CPU_THRESHOLD:
                        send_email(instance_id, avg_cpu)

if __name__ == "__main__":
    check_instance_health()
