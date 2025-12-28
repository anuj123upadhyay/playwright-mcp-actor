# 🎭 Playwright MCP Actor - AI-Powered Browser Automation

**Transform any AI agent into a powerful web scraper in seconds.** Connect Claude, ChatGPT, or custom AI systems directly to browsers for intelligent automation, data extraction, and testing—no coding required for basic tasks.

This Actor enables AI agents to control browsers through the Model Context Protocol (MCP), making web automation as simple as giving natural language instructions. Perfect for scraping dynamic websites, automating workflows, and building AI-powered browser bots that can navigate, extract, and interact with any website.

### 🚀 Why Choose This Actor?

- **AI-Native Design**: Built specifically for AI agents using the Model Context Protocol (MCP)
- **20+ Pre-built Actions**: Navigate, click, fill forms, extract data, screenshots—everything you need
- **5 Ready-to-Use Templates**: Amazon, Google, LinkedIn, Twitter, Google Maps automation out-of-the-box
- **Enterprise-Ready**: Apify Proxy integration, anti-detection stealth mode, unlimited scaling
- **Multiple Export Formats**: JSON, CSV, and Excel exports for business intelligence
- **Zero Setup**: Run immediately with templates or customize for specific needs

---

## 📊 What You Can Build

- **E-commerce Price Monitoring**: Track competitor prices on Amazon, eBay, Shopify
- **Lead Generation**: Extract business data from Google Maps, LinkedIn, Yellow Pages
- **Social Media Monitoring**: Scrape Twitter feeds, LinkedIn profiles, Instagram posts
- **SEO & Market Research**: Analyze Google search results, track rankings, competitor analysis
- **Testing & QA Automation**: Automated browser testing for web applications
- **Data Migration**: Extract data from legacy systems without APIs

---

### What You Get with Apify Platform
| Platform Feature | Benefit |
|-----------------|---------|
| **Apify Proxy** | Rotate IPs automatically, bypass rate limits ($0.10/GB) |
| **Cloud Storage** | Automatic data storage in datasets, no downloads needed |
| **API Access** | Integrate with any system via REST API |
| **Scheduling** | Run daily, hourly, or on-demand |
| **Monitoring** | Email alerts, success/failure tracking |
| **Scaling** | Handle 1 or 1 million requests seamlessly |

---

## 🎯 Quick Start (3 Minutes)

### Option 1: Use a Pre-built Template (Easiest)

```json
{
  "template": "amazon_product_search",
  "template_params": {
    "product_name": "laptop",
    "max_results": 10
  },
  "export_format": "csv"
}
```

**Available Templates:**
- `amazon_product_search` - Search Amazon and extract product details
- `google_search` - Google search with result extraction
- `linkedin_profile` - LinkedIn profile data scraping
- `twitter_scrape` - Twitter/X timeline scraping
- `google_maps_business` - Extract business info from Google Maps

### Option 2: Custom Automation

```json
{
  "browser_type": "chromium",
  "headless": true,
  "stealth_mode": true,
  "actions": [
    {
      "type": "navigate",
      "value": "https://example.com"
    },
    {
      "type": "fill",
      "selector": "#search-box",
      "value": "your search query"
    },
    {
      "type": "click",
      "selector": "button[type='submit']"
    },
    {
      "type": "extract_text",
      "selector": ".results"
    },
    {
      "type": "screenshot"
    }
  ]
}
```

### Option 3: Run via Apify API

```bash
curl https://api.apify.com/v2/acts/aluminum_jam~playwright-mcp-actor/runs \
  -X POST \
  -H "Authorization: Bearer YOUR_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "template": "google_search",
    "template_params": {"search_query": "web scraping"}
  }'
```

---

## 📋 Input Schema

### Basic Configuration

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `browser_type` | string | No | Browser engine: `chromium`, `firefox`, or `webkit` (default: `chromium`) |
| `headless` | boolean | No | Run browser in headless mode (default: `true`) |
| `stealth_mode` | boolean | No | Enable anti-detection features (default: `false`) |
| `export_format` | string | No | Export format: `json`, `csv`, or `excel` (default: `json`) |

### Template Mode (Recommended for Beginners)

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `template` | string | No | Pre-built template name (see list above) |
| `template_params` | object | No | Template-specific parameters |

**Example:**
```json
{
  "template": "amazon_product_search",
  "template_params": {
    "product_name": "wireless mouse",
    "max_results": 20
  }
}
```

### Custom Actions (Advanced Users)

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `actions` | array | Yes* | Array of automation actions (*Required if not using template) |

**Action Object Schema:**
```json
{
  "type": "click",           // Action type (see full list below)
  "selector": "#button",     // CSS selector, XPath, or text
  "value": "text to input",  // Value for fill/type actions
  "selector_type": "auto",   // auto, css, xpath, text, role
  "timeout": 10000           // Timeout in milliseconds
}
```

### Proxy Configuration

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `proxy.use_apify_proxy` | boolean | No | Use Apify's residential proxies |
| `proxy.apify_proxy_groups` | array | No | Proxy groups: `RESIDENTIAL`, `GOOGLE_SERP`, etc. |
| `proxy.custom_proxy_url` | string | No | Custom proxy URL (http://user:pass@host:port) |

**Example with Proxy:**
```json
{
  "proxy": {
    "use_apify_proxy": true,
    "apify_proxy_groups": ["RESIDENTIAL"]
  },
  "template": "google_search",
  "template_params": {
    "search_query": "best laptops 2025"
  }
}
```

---

## 📤 Output Data

### JSON Output (Default)

```json
{
  "success": true,
  "total_actions": 5,
  "successful_actions": 5,
  "failed_actions": 0,
  "total_execution_time_ms": 12450,
  "average_action_time_ms": 2490,
  "screenshots_captured": 1,
  "actions": [
    {
      "type": "navigate",
      "success": true,
      "output": "https://example.com",
      "execution_time_ms": 2340,
      "timestamp": "2025-12-23T16:28:06.123Z"
    },
    {
      "type": "extract_text",
      "selector": ".product-title",
      "success": true,
      "output": "Premium Wireless Mouse - $29.99",
      "execution_time_ms": 145,
      "timestamp": "2025-12-23T16:28:08.468Z"
    }
  ]
}
```

### CSV Export

Set `"export_format": "csv"` to get tabular data:

```csv
type,selector,success,execution_time_ms,timestamp,output
navigate,,true,2340,2025-12-23T16:28:06.123Z,https://example.com
extract_text,.product-title,true,145,2025-12-23T16:28:08.468Z,Premium Wireless Mouse
screenshot,,true,892,2025-12-23T16:28:09.360Z,Screenshot captured (48094 bytes)
```

**Access Exports**: Check the "Key-Value Store" tab for `OUTPUT_CSV.csv` or `OUTPUT_EXCEL.xlsx`

---

## 🎬 Action Types (Complete List)

### Navigation Actions
- `navigate` - Go to URL
- `go_back` - Browser back button
- `go_forward` - Browser forward button
- `reload` - Refresh page
- `get_url` - Get current URL
- `get_title` - Get page title

### Interaction Actions
- `click` - Click element
- `fill` - Fill input (replace content)
- `type` - Type text (append content)
- `select` - Select dropdown option
- `check` - Check checkbox
- `uncheck` - Uncheck checkbox
- `hover` - Hover over element
- `focus` - Focus element
- `press_key` - Press keyboard key (Enter, Escape, etc.)

### Data Extraction
- `extract_text` - Get text content
- `extract_attributes` - Get all element attributes
- `get_html` - Get HTML content
- `screenshot` - Capture full-page screenshot

### Advanced Actions
- `evaluate` - Execute custom JavaScript
- `wait` - Wait for specified time (ms)
- `wait_for_element` - Wait for element to appear
- `scroll` - Scroll page by pixels

---

## 🛡️ Anti-Detection Features

Enable `stealth_mode: true` to activate:

- **WebDriver Property Removal**: Hides automation signals
- **Plugin Mocking**: Simulates real browser plugins
- **Language Spoofing**: Sets realistic language preferences
- **Chrome Object Injection**: Adds genuine Chrome properties
- **Permission API Override**: Mimics human permission patterns
- **Custom User Agent**: Realistic browser fingerprint

**Best for**: Social media scraping, e-commerce sites with bot detection, Google search

---

## 📸 Screenshots & Examples

### Input Configuration Example

![Input Schema](https://via.placeholder.com/800x400/4A90E2/FFFFFF?text=Input+Configuration+Screenshot)

*Configure your automation with simple JSON or use templates for instant results*

### Output Data Example

![Output Data](https://via.placeholder.com/800x400/27AE60/FFFFFF?text=Output+Data+Example)

*Get structured data in JSON, CSV, or Excel format - ready for analysis*

### Apify Console View

![Console Logs](https://via.placeholder.com/800x400/9B59B6/FFFFFF?text=Real-time+Execution+Logs)

*Monitor execution in real-time with detailed progress tracking*

---

## 🎓 Common Use Cases

### 1. E-commerce Price Monitoring

**Track competitor prices across multiple stores:**

```json
{
  "template": "amazon_product_search",
  "template_params": {
    "product_name": "iPhone 15 Pro",
    "max_results": 50
  },
  "stealth_mode": true,
  "export_format": "excel"
}
```


### 2. Lead Generation from Google Maps

**Extract business contact information:**

```json
{
  "template": "google_maps_business",
  "template_params": {
    "search_query": "coffee shops in San Francisco",
    "max_results": 100
  },
  "proxy": {
    "use_apify_proxy": true,
    "apify_proxy_groups": ["GOOGLE_SERP"]
  }
}
```



### 3. Social Media Monitoring

**Track brand mentions on Twitter:**

```json
{
  "template": "twitter_scrape",
  "template_params": {
    "username": "your_brand",
    "max_tweets": 200
  },
  "stealth_mode": true
}
```

**Schedule**: Run every 6 hours
**Cost**: ~$0.10 per run

### 4. SEO Competitor Analysis

**Analyze Google search rankings:**

```json
{
  "template": "google_search",
  "template_params": {
    "search_query": "your target keyword",
    "max_results": 100
  },
  "export_format": "csv"
}
```

**Use**: Track ranking positions, analyze SERP features
**Cost**: ~$0.05 per keyword

---

## 🔧 Advanced Configuration

### Using Custom JavaScript

Execute custom logic with the `evaluate` action:

```json
{
  "type": "evaluate",
  "value": "document.querySelectorAll('.product').length"
}
```

### Handling Dynamic Content

Wait for elements to load:

```json
{
  "type": "wait_for_element",
  "selector": ".product-list",
  "timeout": 30000
}
```

### Taking Targeted Screenshots

Capture specific elements:

```json
{
  "type": "screenshot",
  "selector": ".product-card"
}
```

### Form Automation

Complete multi-step forms:

```json
{
  "actions": [
    {"type": "fill", "selector": "#email", "value": "user@example.com"},
    {"type": "fill", "selector": "#password", "value": "secretpass"},
    {"type": "check", "selector": "#terms"},
    {"type": "click", "selector": "button[type='submit']"},
    {"type": "wait", "value": "3000"},
    {"type": "screenshot"}
  ]
}
```

---

## 🔗 Integration Examples

### Integrate with Make.com (Integromat)

1. Add "HTTP Request" module
2. URL: `\https://api.apify.com/v2/acts/aluminum_jam~playwright-mcp-actor/runs?token=xxxxxxxxxx`
3. Method: POST
4. Headers: `Authorization: Bearer YOUR_API_TOKEN`
5. Body: Your input JSON

### Integrate with Zapier

1. Use "Webhooks by Zapier" action
2. Choose "POST" request
3. URL: `https://api.apify.com/v2/acts/aluminum_jam~playwright-mcp-actor/runs?token=xxxxxxxxx`
4. Add Authorization header
5. Map your data to input schema

### Integrate with Google Sheets

1. Run Actor via API
2. Use Apify Google Sheets integration
3. Auto-export results to spreadsheet
4. Schedule for automatic updates

---

## 📊 Performance & Limits

### Speed Benchmarks
- **Simple navigation**: 2-4 seconds
- **Form filling**: 0.5-1 second per field
- **Data extraction**: 0.1-0.5 seconds per element
- **Screenshot**: 0.5-2 seconds

### Recommended Limits
- **Max actions per run**: 100 (for optimal performance)
- **Timeout per action**: 30 seconds (default: 10 seconds)
- **Max run time**: 300 seconds (5 minutes)
- **Concurrent runs**: Up to 100 (depending on plan)

### Resource Usage
- **Memory**: 512MB - 1GB per run
- **CPU**: 1 core per run
- **Storage**: 100MB per run (includes screenshots)

---

## 🆘 Troubleshooting & Support

### Common Issues

#### Element Not Found
**Problem**: `Element not found or timeout` error

**Solutions:**
1. Increase timeout: `"timeout": 30000`
2. Try different selector: Use browser DevTools to find correct selector
3. Wait for element: Add `wait_for_element` action first
4. Use text selector: `"selector": "Button Text", "selector_type": "text"`

#### Proxy Errors
**Problem**: `Proxy connection failed`

**Solutions:**
1. Verify Apify Proxy is enabled in your account
2. Check proxy group availability: Try `RESIDENTIAL` or remove groups for `auto`
3. Test without proxy first to isolate issue

#### Rate Limiting / Blocked
**Problem**: Website blocks requests

**Solutions:**
1. Enable stealth mode: `"stealth_mode": true`
2. Use Apify Proxy: `"use_apify_proxy": true`
3. Add delays: Insert `wait` actions between requests
4. Reduce concurrent runs

#### Data Export Issues
**Problem**: Export file not found

**Solutions:**
1. Check "Key-Value Store" tab in Apify console
2. File is named `OUTPUT_CSV.csv` or `OUTPUT_EXCEL.xlsx`
3. Ensure `export_format` is set correctly

### Need Help?

1. **GitHub Issues**: [Report bugs or request features](https://github.com/anuj123upadhyay/playwright-mcp-actor/issues)
2. **Apify Forum**: [Community support](https://community.apify.com)
3. **Email Support**: anuju760@gmail.com (for paid users)


### Known Limitations

- **CAPTCHA**: Cannot solve CAPTCHAs automatically (use CAPTCHA solving integration)
- **Login Required**: Some sites require authenticated sessions (use cookies)
- **Heavy JavaScript**: Complex SPAs may need additional wait times
- **Bot Detection**: Some sites actively block automation (use stealth mode + proxies)

---

## ⚖️ Legal & Compliance

### Terms of Service Compliance

**Important**: This tool automates browser interactions. You are responsible for complying with:
- Website Terms of Service you're accessing
- Robots.txt directives
- Rate limiting policies
- Data protection laws (GDPR, CCPA)
- Copyright and intellectual property rights

### Best Practices

✅ **DO:**
- Respect robots.txt files
- Use reasonable request rates
- Add proper User-Agent headers
- Cache results to minimize requests
- Review website ToS before scraping

❌ **DON'T:**
- Scrape personal data without consent
- Bypass authentication without permission
- Ignore rate limits
- Redistribute scraped data commercially without rights
- Use for malicious purposes

**Disclaimer**: The authors are not responsible for misuse of this tool. Users must ensure compliance with all applicable laws and regulations.

---

## 🚀 Related Actors & Tools

Maximize your workflows with these complementary Actors:

| Actor | Use Case | Link |
|-------|----------|------|
| **Cheerio Scraper** | Fast HTML parsing | [View Actor](https://apify.com/apify/cheerio-scraper) |
| **Puppeteer Scraper** | Alternative browser automation | [View Actor](https://apify.com/apify/puppeteer-scraper) |
| **Web Scraper** | Point-and-click scraping | [View Actor](https://apify.com/apify/web-scraper) |
| **Google Sheets Export** | Export to spreadsheets | [View Integration](https://apify.com/integrations/google-sheets) |
| **CAPTCHA Solver** | Solve CAPTCHAs | [View Actor](https://apify.com/apify/captcha-solver) |

**Build a complete workflow**: Use this Actor for data extraction → Process with custom scripts → Export to Google Sheets → Visualize in Tableau

---

## 💬 Custom Solutions & Enterprise Support

Need something more tailored to your business?

### We Offer:
- **Custom Template Development**: We build templates for your specific use case
- **Integration Services**: Connect with your existing tools and databases
- **Dedicated Support**: Priority support with SLA guarantees
- **Training & Consulting**: Team training on web scraping best practices
- **Managed Scraping**: We handle everything for you

**Contact**: anuju760@gmail.com 
---

## 📈 Changelog

### v1.0.0 (December 2025)
- ✅ Initial release
- ✅ 20+ action types
- ✅ 5 pre-built templates
- ✅ CSV/Excel export
- ✅ Apify Proxy integration
- ✅ Anti-detection stealth mode

### Upcoming Features
- 🔜 AI action generator (natural language → actions)
- 🔜 CAPTCHA solving integration
- 🔜 Cookie session management
- 🔜 Advanced scheduling options
- 🔜 Webhook notifications


---

## 📞 Contact

- **Email**: anuju760@gmail.com
- **Twitter**: [@anuj123upadhyay](https://x.com/anuj123upadhyay)
- **GitHub**: [@anuj123upadhyay](https://github.com/anuj123upadhyay/playwright-mcp-actor)

---

**Made with ❤️ for the Apify community** | [Report Issues](https://github.com/anuj123upadhyay/playwright-mcp-actor/issues) | [Request Features](https://github.com/anuj123upadhyay/playwright-mcp-actor/issues/new) | [⭐ Star on GitHub](https://github.com/anuj123upadhyay/playwright-mcp-actor)


---


