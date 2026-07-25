# MIC NSW Website - Setup Instructions

## 🔴 CRITICAL SETUP (Must Do Before Going Live)

### Step 1: Get Web3Forms API Key

1. Go to: https://web3forms.com
2. Enter your email: info@mic-nsw.com.au
3. You'll receive an access key via email
4. Copy that key and save it

### Step 2: Add Web3Forms Key to Website

**In index.html (line ~480):**
```html
<input type="hidden" name="access_key" value="PASTE_YOUR_KEY_HERE">
```

**In build-your-renovation.html (line ~825):**
```javascript
const WEB3FORMS_ACCESS_KEY = 'PASTE_YOUR_KEY_HERE';
```

**Replace `PASTE_YOUR_KEY_HERE` with your actual Web3Forms key.**

---

## 🟡 RECOMMENDED SETUP (Should Do)

### Step 3: Create Images Folder & Upload Logos

1. Create a new folder in your GitHub repo called `images`
2. Download your logos from: https://mic-nsw.com.au/front/images/
   - logo.png
   - logo2.png
   - logo3.png
3. Upload them to the `images/` folder
4. The HTML files already use relative paths (`images/logo2.png`)

### Step 4: Enable Google Analytics (Optional)

1. Go to: https://analytics.google.com
2. Create a GA4 property
3. Copy your Measurement ID (e.g., `G-ABC123XYZ`)
4. In `index.html`, find the commented GA4 block and uncomment it
5. Replace `G-XXXXXXXXXX` with your actual ID

---

## 🟢 OPTIONAL SETUP

### Step 5: Update Pricing (If Confirmed)

Update these in both `index.html` and `build-your-renovation.html`:

**Kitchen:**
- Essential: $18,000 – $28,000
- Premium: $35,000 – $55,000
- Luxury: $65,000 – $110,000

**Bathroom:**
- Essential: $18,000 – $26,000
- Premium: $28,000 – $45,000
- Luxury: $50,000 – $80,000

### Step 6: Update Supplier Brands

In `build-your-renovation.html`, update these arrays with your actual suppliers:
- `kitchenPackages[]`
- `bathroomPackages[]`
- `benchtops[]`
- `microwaves[]`
- `ovens[]`
- `cooktops[]`
- `rangehoods[]`
- `tapware[]`

---

## ✅ Testing Checklist

After each change, test at: https://moathmhdi12.github.io/Master

- [ ] Contact form submits (should show "Thanks" message)
- [ ] Logo images load (should appear in header & footer)
- [ ] Design studio loads and works
- [ ] All prices display correctly
- [ ] Mobile menu works
- [ ] All links are functional
- [ ] No console errors (F12 → Console)

---

## 📋 Files Modified

- ✅ `index.html` - Added Web3Forms form, GA4 placeholder, fixed image paths
- ✅ `build-your-renovation.html` - Added Web3Forms quote handling, fixed image paths
- ✅ `sitemap.xml` - Already configured
- ✅ `robots.txt` - Already configured

---

## 🚀 Deployment Steps

1. Complete all CRITICAL setup (Step 1-2)
2. Test contact form locally
3. Commit changes to GitHub
4. Website updates at: https://moathmhdi12.github.io/Master
5. Submit `sitemap.xml` to Google Search Console
6. Configure custom domain if needed

---

## 💬 Quick Questions?

All external resources (fonts, icons) come from trusted CDNs:
- Fonts: Google Fonts (fonts.googleapis.com)
- WhatsApp links: wa.me (official WhatsApp service)
- Web forms: Web3Forms (email backend service)
- Analytics: Google Analytics 4 (optional)

---

**Ready to go live?** Follow the steps above, then your site will be fully functional! 🎉
