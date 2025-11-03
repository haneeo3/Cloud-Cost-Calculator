
# Cloud Cost Calculator

This project helps you **watch how much money you spend on AWS**.
It uses **CloudWatch**, **Lambda**, **SNS**, and **S3** to send you alerts when your AWS bill gets too high.

**Example:**
If you want to know when your AWS cost passes **$20 per day**, this system will check your spending every day and send you a message when that happens.

---

## Problem

Many people get surprised by high AWS bills.
You may start a small project and forget to stop some services, then at the end of the month, you see a big bill.

AWS has a billing page, but it doesn’t send alerts fast or explain which service is using the most money.
Checking it by hand every day is slow and boring.

**Main problems:**

* You don’t get alerts when your cost increases suddenly.
* It’s hard to know which service (like EC2, S3, or Lambda) is causing high costs.
* Doing it manually wastes time and can cause money loss.

---

## Solution

**Cloud Cost Calculator** fixes that by watching your AWS spending automatically.
It runs every day, checks your costs, and tells you if you go over your limit.

**How it works:**

* **CloudWatch** collects your daily cost from AWS.
* **Lambda** is a small program that checks your spending.
* **SNS** sends you an alert by email or SMS when your cost is too high.
* **S3** saves all your reports so you can look back later.

**Example:**
Let’s say you spend **$10 on Monday**, **$15 on Tuesday**, and your limit is **$12**.
The system will send you an alert on Tuesday saying:
“Your AWS cost today is $15. You crossed your $12 limit.”

---

## Why This Way

* **No extra servers:** Lambda only runs when needed, so you don’t pay for idle time.
* **All AWS tools:** Everything uses built-in AWS services. No external software.
* **Easy to grow:** Works for small or big projects.
* **Automatic:** Once you set it up, it runs by itself.

---

## Architecture (How it connects)

* **CloudWatch** watches the cost and sends data.
* **Lambda** checks the data once per day.
* **SNS** sends alerts if needed.
* **S3** stores your cost history.

```
[CloudWatch] → [Lambda] → [SNS]
                     ↓
                   [S3]
```

---

## Setup Steps

### 1. Create an S3 bucket

Name it something like **aws-cost-logs**.
It will save your data.

### 2. Create an SNS topic

This is where alerts go.
Add your **email** or **phone number** to get messages.

### 3. Create a Lambda function

* Use **Python 3.12**
* Give it permission to use **CloudWatch**, **S3**, and **SNS**

### 4. Set CloudWatch to run Lambda daily

Add a rule in **CloudWatch Events** to trigger the Lambda function once a day.

### 5. Test it

Run Lambda manually the first time.
You should get an alert if the cost passes your limit.

---

## Example Alert

**Email Subject:** AWS Cost Alert
**Email Message:**
Your total AWS cost for today is **$22.45**, which is more than your limit of **$20.00**.


cloud-cost-calculator/
│
├── lambda/
│   └── daily_cost_checker.py       Lambda function code
│
├── events/
│   └── test_event.json             Sample test event for Lambda
│
├── docs/
│   └── sns_alert_example.png       Screenshot of SNS email alert
│
└── README.md   
---

## Ideas for Later

* Show a **chart of cost trends** using QuickSight or Grafana.
* Add **warning levels**, like yellow for $10 and red for $20.
* Send alerts to **Slack** or **Microsoft Teams**.
* Add a **dashboard** to view cost reports directly.
* Use **AI (Bedrock)** to predict next month’s cost.
* Add **multiple users** so team members can get their own alerts.
