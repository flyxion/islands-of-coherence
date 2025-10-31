---
title: Add a Comment System
layout: default
---

# How to Add Comments to Islands of Coherence

This guide adds a **privacy-first comment system** using **[utterances](https://utteranc.es/)** — a lightweight, open-source solution that stores comments as **GitHub Issues**.

---

## Why utterances?

| Feature | Benefit |
|-------|--------|
| **GitHub Issues backend** | No external database, full moderation |
| **No tracking** | GDPR-compliant, no ads |
| **Markdown support** | Rich comments |
| **Dark mode** | Matches your theme |
| **Free & open** | MIT licensed |

---

## Step 1: Create a Public GitHub Repository

1. Go to [github.com/new](https://github.com/new)
2. Name: `islands-of-coherence-comments`
3. Check **"Public"**
4. Click **"Create repository"**

> This repo will store all comments as issues.

---

## Step 2: Enable Issues

1. In the new repo → **Settings** → **General**
2. Under **Features**, enable **"Issues"**

---

## Step 3: Install the utterances App

1. Go to: [https://github.com/apps/utterances](https://github.com/apps/utterances)
2. Click **"Install"**
3. Select **Only select repositories**
4. Choose `islands-of-coherence-comments`
5. Click **"Install"**

> You now have permission to post issues as comments.

---

## Step 4: Get the Embed Code

1. Go to: [https://utteranc.es](https://utteranc.es)
2. Fill in:
   - **Repository**: `flyxion/islands-of-coherence-comments`
   - **Issue mapping**: `pathname` *(recommended)*
   - **Theme**: `github-light` or `photon-dark`
3. Copy the generated `<script>` tag

---

## Step 5: Add to Your Site

### Option A: Site-Wide (All Pages)

Edit `docs/_layouts/default.html` and add **before `</body>`**:

```html
<!-- Utterances Comments -->
<script src="https://utteranc.es/client.js"
        repo="flyxion/islands-of-coherence-comments"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
