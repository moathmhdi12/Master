# MIC NSW Website - Copilot Quick Fixes

## How to Use This Document

Copy ONE section at a time and paste it into Copilot. Wait for the response, review the changes, then proceed to the next fix.

---

## 🔴 CRITICAL FIX #1: Add Web3Forms Key to index.html

**Send this to Copilot:**

```
In my GitHub repo moathmhdi12/Master, file index.html:

Find this line (around line 480, in the contact form):
<input type="hidden" name="access_key" value="PASTE_YOUR_KEY_HERE">

Replace PASTE_YOUR_KEY_HERE with: YOUR_ACTUAL_WEB3FORMS_KEY

Show me the exact line after the replacement, then commit the change.
```

**Before you send:**
1. Get your Web3Forms key from https://web3forms.com (enter info@mic-nsw.com.au)
2. Replace `YOUR_ACTUAL_WEB3FORMS_KEY` with the actual key
3. Send to Copilot

---

## 🔴 CRITICAL FIX #2: Add Web3Forms Key to build-your-renovation.html

**Send this to Copilot:**

```
In my GitHub repo moathmhdi12/Master, file build-your-renovation.html:

Find this line (around line 825, in the JavaScript section):
const WEB3FORMS_ACCESS_KEY = 'PASTE_YOUR_KEY_HERE';

Replace PASTE_YOUR_KEY_HERE with: YOUR_ACTUAL_WEB3FORMS_KEY

(Same key as in index.html)

Show me the exact line after the replacement, then commit the change.
```

---

## 🟡 RECOMMENDED FIX #3: Update Image Paths

**Send this to Copilot:**

```
In both index.html and build-your-renovation.html:

Replace all instances of:
https://mic-nsw.com.au/front/images/logo2.png

With:
images/logo2.png

Also replace:
https://mic-nsw.com.au/front/images/logo3.png

With:
images/logo3.png

Show me all lines that were changed, then commit.
```

**Before you send:**
- Make sure you've created an `images/` folder in your GitHub repo
- Upload logo2.png and logo3.png to that folder

---

## 🟢 OPTIONAL FIX #4: Enable Google Analytics

**Send this to Copilot:**

```
In index.html, find the commented-out Google Analytics 4 block:

<!-- Google Analytics 4 ... -->
<!--
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script> window.dataLayer = window.dataLayer || []; function gtag(){dataLayer.push(arguments);} gtag('js', new Date()); gtag('config', 'G-XXXXXXXXXX'); </script>
-->

Uncomment it by removing the <!-- and --> markers.

Then replace both instances of G-XXXXXXXXXX with: G-YOUR_MEASUREMENT_ID

Show me the before and after, then commit.
```

**Before you send:**
1. Go to https://analytics.google.com
2. Create a GA4 property for your website
3. Copy your Measurement ID (looks like: G-ABC123XYZ)
4. Replace `G-YOUR_MEASUREMENT_ID` with that ID

---

## 🟢 OPTIONAL FIX #5: Update Pricing

**Send this to Copilot:**

```
In index.html, update all kitchen and bathroom package prices:

KITCHEN:
- Replace: $18,000 – $28,000 with: YOUR_KITCHEN_ESSENTIALS_PRICE
- Replace: $35,000 – $55,000 with: YOUR_KITCHEN_PREMIUM_PRICE
- Replace: $65,000 – $110,000 with: YOUR_KITCHEN_LUXURY_PRICE

BATHROOM:
- Replace: $18,000 – $26,000 with: YOUR_BATHROOM_ESSENTIALS_PRICE
- Replace: $28,000 – $45,000 with: YOUR_BATHROOM_PREMIUM_PRICE
- Replace: $50,000 – $80,000 with: YOUR_BATHROOM_LUXURY_PRICE

Also in build-your-renovation.html, update the kitchenPackages and bathroomPackages arrays with matching prices.

Show me all changes, then commit.
```

**Before you send:**
- Get actual prices from MIC NSW
- Format them as: $LOW – $HIGH (e.g., $20,000 – $30,000)

---

## 🟢 OPTIONAL FIX #6: Update Supplier Brands

**Send this to Copilot:**

```
In build-your-renovation.html, update these supplier arrays with actual MIC NSW suppliers:

benchtops = [ ... ]
  Current: Laminex, Essastone, Caesarstone, Smartstone, Dekton
  Update to: YOUR_ACTUAL_BRANDS

microwaves = [ ... ]
  Current: Chef, Bosch, Miele
  Update to: YOUR_ACTUAL_BRANDS

ovens = [ ... ]
  Current: Westinghouse, Fisher & Paykel, ILVE, Miele
  Update to: YOUR_ACTUAL_BRANDS

cooktops = [ ... ]
  Current: Chef, Bosch, Miele
  Update to: YOUR_ACTUAL_BRANDS

rangehoods = [ ... ]
  Current: Chef, Fisher & Paykel, Miele
  Update to: YOUR_ACTUAL_BRANDS

tapware = [ ... ] (bathroom section)
  Current: Caroma, Nero, Sussex, Phoenix
  Update to: YOUR_ACTUAL_BRANDS

Show me each array after the update, then commit.
```

**Before you send:**
- Confirm actual supplier brands with MIC NSW
- Make a list of what each category should be

---

## ✅ Order to Send Fixes

1. **FIX #1** (Web3Forms key in index.html) — CRITICAL
2. **FIX #2** (Web3Forms key in build-your-renovation.html) — CRITICAL
3. **FIX #3** (Image paths) — RECOMMENDED
4. **FIX #4** (Google Analytics) — OPTIONAL
5. **FIX #5** (Pricing) — OPTIONAL (only if confirmed)
6. **FIX #6** (Suppliers) — OPTIONAL (only if confirmed)

---

## 🧪 Testing After Each Fix

After Copilot commits each fix:

1. Wait 1-2 minutes
2. Visit: https://moathmhdi12.github.io/Master
3. Check:
   - Contact form appears (FIX #1-2)
   - Logo images load (FIX #3)
   - No console errors (F12 → Console tab)
   - Prices show correctly (FIX #5)
   - Brand names are right (FIX #6)

---

## 💡 Pro Tips

- Copy the EXACT text in the code blocks
- Replace placeholders (like `YOUR_ACTUAL_WEB3FORMS_KEY`) with real values
- Always review Copilot's response before approving
- If something looks wrong, ask Copilot to fix it
- Test the live site after each change

---

## 🚀 You're Done When

- ✅ Web3Forms key added (FIX #1-2)
- ✅ Contact form works
- ✅ Images load
- ✅ No errors in console
- ✅ Live site looks good

**Then you're ready to go live!** 🎉
