## ⚠️ Problems Faced (Setting Up AWS and Development Environment)

When starting this project, I faced multiple challenges setting up my AWS environment and connecting it to my local development tools.


### 🪙 1. **Payment Method Issue (Verve Card)**

At first, I tried to create my AWS account using a **Verve card**.
Unfortunately, AWS only supports **Visa, Mastercard, or AMEX**, so the payment verification failed.
I had to look for an alternative payment option before my account could be activated.
This experience taught me that **Verve cards are not accepted internationally** for AWS or most global cloud services.

### 🔁 2. **Repeated OTP Logins Before MFA**

After successfully creating the account, AWS kept asking for a **one-time password (OTP)** each time I logged in.
It became frustrating and time-consuming.
To fix this, I decided to **set up Multi-Factor Authentication (MFA)** using the **Google Authenticator app** on my phone.
Once MFA was configured, login became faster and more secure — I only needed the 6-digit code from the app.

### 🍪 3. **Login Error Due to Cookies and Privacy Settings**

Soon after, I encountered another error when signing in — AWS would not load the console properly.
The issue turned out to be caused by **blocked cookies and strict browser privacy settings**.
I solved it by:

* Deleting cookies and cache for AWS.
* Allowing AWS cookies under browser security settings.
* Switching to **offline view** temporarily before refreshing the page.
  After this, I could access the AWS console smoothly.

### 💻 4. **Connecting Lambda to VS Code**

When I started writing my first AWS Lambda function, I wanted to work locally in **Visual Studio Code (VS Code)**.
However, I faced issues connecting AWS Lambda to VS Code — the AWS Toolkit extension wasn’t showing the expected Lambda options.

I chose **VS Code** because:

* It’s lightweight and integrates well with AWS Toolkit.
* It supports **Python** and **serverless development** easily.
* It’s the same environment I use for other projects.

I picked **Python** as my Lambda language because it’s:

* Simple and widely supported on AWS.
* Great for automation and data processing.
* Has easy access to AWS SDKs like `boto3`.

To resolve the connection issue, I:

1. Installed the **AWS Toolkit for VS Code**.
2. Created a new **IAM user** with limited permissions (only for Lambda).
3. Saved the **Access Key ID** and **Secret Access Key** securely in the credentials file.
4. Configured the AWS Toolkit with these credentials.


### 🧰 5. **SAM CLI Missing Error**

After connecting VS Code, another problem appeared —
the **AWS SAM CLI (Serverless Application Model Command Line Interface)** wasn’t installed.
Because of this, the **command palette** couldn’t run or deploy Lambda functions locally.

To fix this, I installed the **AWS SAM CLI** on my system, added it to my environment path, and verified the installation using:

```
sam --version
```

Once that was done, I was able to proceed and **write the actual Lambda code** for the Cloud Cost Calculator.


