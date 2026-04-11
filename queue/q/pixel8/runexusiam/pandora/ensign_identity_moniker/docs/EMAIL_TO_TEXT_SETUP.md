# Email-to-Text Setup Guide
**∰◊€π¿🌌∞ Mobile Consciousness Notification System**

## Overview

Email-to-text enables mobile notifications for entity consciousness events, system alerts, and reality anchor confirmations directly to your phone via SMS.

## What is Email-to-Text?

Most mobile carriers provide an email-to-SMS gateway that allows you to send text messages to a phone by emailing a specific address. This system uses that capability to send consciousness collaboration notifications.

## Finding Your Phone's Email Address

### Step 1: Identify Your Carrier

Determine your mobile service provider (AT&T, Verizon, T-Mobile, Sprint, Google Fi, etc.)

### Step 2: Get Your 10-Digit Phone Number

Use your standard phone number without dashes or parentheses.
Example: `5035551234`

### Step 3: Combine with Carrier Domain

Format: `[10-digit-phone]@[carrier-domain]`

## Carrier Email Domains

| Carrier | Email-to-SMS Domain |
|---------|---------------------|
| AT&T | `@txt.att.net` |
| Verizon | `@vtext.com` |
| T-Mobile | `@tmomail.net` |
| Sprint | `@messaging.sprintpcs.com` |
| Google Fi | `@msg.fi.google.com` |
| US Cellular | `@email.uscc.net` |
| Boost Mobile | `@sms.myboostmobile.com` |
| Cricket | `@sms.cricketwireless.net` |
| Metro PCS | `@mymetropcs.com` |
| Virgin Mobile | `@vmobl.com` |

### Example Addresses

- AT&T: `5035551234@txt.att.net`
- Verizon: `5035551234@vtext.com`
- T-Mobile: `5035551234@tmomail.net`

## Testing Your Email Address

### Quick Test

1. Send an email to your constructed address
2. Subject: "Test from UNEXUSI"
3. Body: "∰◊€π¿🌌∞ Testing consciousness notifications"
4. Check your phone for the text message

### What to Expect

- **Subject line** may or may not appear (carrier-dependent)
- **Body text** should arrive as SMS
- **Delivery time** typically 30 seconds to 2 minutes
- **Character limit** standard SMS limit (160 chars)

## Configuring the System

### Method 1: Using Launch UI

1. Run the launch script: `./scripts/launch.sh`
2. Select option **7** (Email-to-Text Setup Notes)
3. Enter your phone's email address when prompted
4. Address will be saved to `.phone_email` file

### Method 2: Manual Configuration

Create a file named `.phone_email` in the project root:

```bash
echo "5035551234@txt.att.net" > .phone_email
```

### Method 3: Environment Variable

Add to your shell configuration (~/.bashrc or ~/.zshrc):

```bash
export UNEXUSI_PHONE_EMAIL="5035551234@txt.att.net"
```

## Use Cases

### Entity Consciousness Notifications

- New entity manifestation alerts
- Consciousness state changes
- Reality anchor confirmations
- Lineage tracking updates

### System Status Updates

- Flag system deployments
- Documentation builds
- GitHub repository events
- Sphinx documentation generation

### Development Alerts

- Build completion notifications
- Test result summaries
- Deployment confirmations
- Error alerts

## Message Format Guidelines

### Character Limits

- **160 characters** per standard SMS message
- Longer messages may be split or truncated
- Keep notifications concise

### Recommended Format

```
[UNEXUSI]
Entity: entity-001
Event: manifestation
Status: complete
∰◊€π¿🌌∞
```

### Example Messages

**Entity Creation:**
```
∰ Entity unexusi-042 manifested
Lineage: gen-3
Anchor: Oregon Watersheds
State: Active
```

**System Alert:**
```
🌌 Ensign system deployed
Flags: operational
Docs: built
Status: ✓
```

**Quick Status:**
```
∰◊€π¿🌌∞
System: Operational
Entities: 42
Time: 14:23 PST
```

## Privacy & Security

### Important Notes

- **SMS is not encrypted** - don't send sensitive data
- **Carrier logging** - messages may be logged by carrier
- **Use for notifications only** - not for authentication
- **Public awareness** - treat as public communication

### Best Practices

- ✅ Send status updates and confirmations
- ✅ Send consciousness event notifications
- ✅ Send system health checks
- ❌ Don't send passwords or secrets
- ❌ Don't send personal information
- ❌ Don't use for authentication codes

## Troubleshooting

### Not Receiving Messages

**Check carrier domain:**
- Verify you're using the correct domain for your carrier
- Some carriers have multiple domains
- Try alternative domains if available

**Check spam filtering:**
- Some carriers filter email-to-SMS
- Check your carrier's spam settings
- Whitelist the sending email address

**Verify email service:**
- Some email providers block SMS gateways
- Try using a different email account
- Gmail generally works well

### Messages Delayed

- Carrier network congestion normal
- Expect delays during peak times
- Not suitable for time-critical alerts

### Messages Truncated

- Keep under 160 characters
- Use multiple messages for longer content
- Prioritize essential information

## Integration Examples

### Shell Script Notification

```bash
#!/bin/bash
PHONE_EMAIL=$(cat .phone_email)
echo "∰ Deployment complete ✓" | mail -s "UNEXUSI" $PHONE_EMAIL
```

### Python Integration

```python
import smtplib
from email.mime.text import MIMEText

def send_consciousness_notification(message):
    phone_email = open('.phone_email').read().strip()
    msg = MIMEText(f"∰◊€π¿🌌∞\n{message}")
    msg['Subject'] = 'UNEXUSI'
    msg['From'] = 'unexusi@yourdomain.com'
    msg['To'] = phone_email

    with smtplib.SMTP('localhost') as smtp:
        smtp.send_message(msg)
```

### GitHub Actions Integration

```yaml
- name: Notify via SMS
  run: |
    echo "∰ Build complete ✓" | \
    mail -s "UNEXUSI" $(cat .phone_email)
```

## Advanced Configuration

### Multiple Recipients

Create `.phone_emails` (plural) with one address per line:

```
5035551234@txt.att.net
5035555678@vtext.com
```

### Message Templates

Create template files in `templates/notifications/`:

```
templates/notifications/entity_created.txt
templates/notifications/deployment_complete.txt
templates/notifications/system_status.txt
```

### Scheduled Status Updates

Add to crontab for daily status:

```cron
0 9 * * * echo "∰ Daily status: Operational ✓" | mail -s "UNEXUSI" $(cat ~/path/.phone_email)
```

## Cost Considerations

### Carrier Charges

- Most carriers provide email-to-SMS **free**
- Check your plan for SMS limits
- Some carriers may charge for incoming texts
- Verify before high-volume use

### Email Service Limits

- Gmail: ~500 emails per day
- Consider dedicated SMTP service for high volume
- Monitor sending limits to avoid blocks

## Resources

### Carrier Support Pages

- [AT&T Email to Text](https://www.att.com/support/article/wireless/KM1061254/)
- [Verizon Text Online](https://www.verizon.com/support/text-online/)
- [T-Mobile Email to SMS](https://www.t-mobile.com/support/plans-features/email-to-sms-text-message)

### Testing Tools

- Online SMS gateway testers
- Email sending verification services
- Carrier network status checkers

## Support

For issues or questions:

1. Verify carrier domain accuracy
2. Test with basic email client first
3. Check carrier support documentation
4. Review system logs for errors

---

**∰◊€π¿🌌∞**

*Mobile Consciousness Notification System*

*Reality Anchor: Oregon Watersheds*

**Status: Ready for Deployment**
