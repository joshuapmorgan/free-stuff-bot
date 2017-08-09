# free-stuff-bot

## Build

To build:

```console
$ make
```

Recommended to build on EC2 instance using amzn-ami-hvm-2016.03.3.x86_64-gp2 AMI, as lxml dependency includes source files that ultimately are linked into some ELF shared objects.

## Environment

WEBHOOK_URL must be configured with the Slack Incoming Webhook URL.

## TODO

 - Makefile target for release (utilise AWS CLI to update Lambda function)
 - Error handling
