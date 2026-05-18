# Test Report — Login Module

| Test ID | Module | Test Case | Category | Preconditions | Steps | Expected Result | Actual Result | Status | Priority | Notes |
|---------|--------|-----------|----------|---------------|-------|-----------------|---------------|--------|----------|-------|
| TC-01 | Login | Login page loads successfully | Happy Path | App running at localhost:5173 | 1. Navigate to / 2. Check page title 3. Verify form elements visible | Page title contains "ShopEY", sign-in heading visible, email/password inputs and submit button present | — | Ready to Execute | High | Core page load verification |
| TC-02 | Login | Login with valid credentials shows success | Happy Path | Registered user exists | 1. Register user via API 2. Fill email 3. Fill password 4. Click Sign In | Success toast "Welcome back" appears | — | Ready to Execute | High | Primary login flow |
| TC-03 | Login | Login with invalid email format shows error | Validation | App running | 1. Enter invalid email format 2. Enter password 3. Click Sign In | Inline error "Invalid email format" shown | — | Ready to Execute | High | Client-side validation |
| TC-04 | Login | Login with wrong password shows error | Error Handling | App running | 1. Enter valid email format 2. Enter wrong password 3. Click Sign In | Error banner "Invalid email or password" displayed | — | Ready to Execute | High | Server-side error handling |
| TC-05 | Login | Login with empty fields shows validation errors | Validation | App running | 1. Leave email empty 2. Leave password empty 3. Click Sign In | "Email is required" and "Password is required" errors shown | — | Ready to Execute | High | Required field validation |
| TC-06 | Login | Password show/hide toggle works | UI/UX | App running | 1. Enter password 2. Click eye toggle 3. Verify type=text 4. Click again 5. Verify type=password | Password visibility toggles between hidden and visible | — | Ready to Execute | Medium | Accessibility feature |
| TC-07 | Registration | Can switch to registration form | Navigation | App running on login form | 1. Click "Sign up" link | Registration form displayed with all fields (first name, last name, email, password, confirm password) | — | Ready to Execute | High | Form navigation |
| TC-08 | Registration | Register with valid data succeeds | Happy Path | App running, email not taken | 1. Switch to register 2. Fill all fields with valid data 3. Click Register | Success toast "Account created successfully", redirected to login form | — | Ready to Execute | High | Primary registration flow |
| TC-09 | Registration | Register with duplicate email shows conflict error | Error Handling | User already registered with email | 1. Register user via API 2. Try same email via UI form 3. Click Register | Error "Email already registered" shown | — | Ready to Execute | High | 409 Conflict handling |
| TC-10 | Registration | Register with weak password shows validation error | Validation | App running | 1. Switch to register 2. Fill fields with weak password ("weak") 3. Click Register | Error "Password must be at least 8 characters" shown | — | Ready to Execute | High | Password strength validation |
| TC-11 | Registration | Register with mismatched passwords shows error | Validation | App running | 1. Switch to register 2. Enter password 3. Enter different confirm password 4. Click Register | Error "Passwords do not match" shown | — | Ready to Execute | High | Confirm password validation |
| TC-12 | Registration | All registration fields are required | Validation | App running on register form | 1. Switch to register 2. Click Register without filling any fields | All required field errors shown (first name, last name, email, password, confirm) | — | Ready to Execute | High | Required fields enforcement |
| TC-13 | UI/UX | Branding panel is visible on desktop | UI/UX | Desktop viewport (1280x800) | 1. Set viewport to 1280x800 2. Navigate to / 3. Check branding panel | Branding panel visible with "Future of Shopping" headline | — | Ready to Execute | Medium | Desktop layout verification |
| TC-14 | UI/UX | Branding panel hidden on mobile viewport | Responsive | Mobile viewport (375x667) | 1. Set viewport to 375x667 2. Navigate to / 3. Check branding panel | Branding panel hidden, form still visible and usable | — | Ready to Execute | Medium | Responsive design verification |
| TC-15 | UI/UX | Form animations are smooth (no layout shift) | UI/UX | App running | 1. Navigate to / 2. Record form position 3. Switch to register 4. Compare positions | Form card X position remains stable (< 5px shift) | — | Ready to Execute | Low | Animation quality check |

---

# Test Report — Home Page

| Test ID | Module | Test Case | Category | Preconditions | Steps | Expected Result | Actual Result | Status | Priority | Notes |
|---------|--------|-----------|----------|---------------|-------|-----------------|---------------|--------|----------|-------|
| TC-16 | Navigation | Navbar is visible with logo, menu links, search, cart, user icons | UI/UX | App running at localhost:5173 | 1. Navigate to / 2. Check navbar visibility 3. Verify logo, 5 nav links, search, cart, user icons | Navbar visible with ShopEY logo, Home/Shop/Categories/About/Contact links, search/cart/user icons | — | Ready to Execute | High | Core navigation verification |
| TC-17 | Navigation | Navbar becomes solid on scroll | UI/UX | App running | 1. Navigate to / 2. Scroll page past 60px 3. Check navbar class | Navbar gains "scrolled" class creating solid background | — | Ready to Execute | Medium | Scroll behavior |
| TC-18 | Navigation | Menu links are clickable | Navigation | App running | 1. Navigate to / 2. Click each nav link (Home, Shop, Categories, About, Contact) | Each link has valid href and clicking does not navigate away from page | — | Ready to Execute | Medium | Anchor link navigation |
| TC-19 | Navigation | Cart icon shows badge when items in cart | UI/UX | User logged in with items in cart | 1. Register/login user 2. Add product to cart via API 3. Set token in localStorage 4. Reload page | Cart badge visible with item count > 0 | — | Ready to Execute | High | Cart state display |
| TC-20 | Hero | Hero section displays headline, subheading, and CTA buttons | UI/UX | App running | 1. Navigate to / 2. Check hero section content | Hero shows "Discover the Latest Trends" title, subtitle, "Shop Now" and "Explore Categories" buttons | — | Ready to Execute | High | Main hero content |
| TC-21 | Hero | CTA "Shop Now" button scrolls to products section | Navigation | App running | 1. Navigate to / 2. Click "Shop Now" button | Page scrolls to featured products section (in viewport) | — | Ready to Execute | Medium | CTA functionality |
| TC-22 | Categories | Categories are loaded and displayed from API | Happy Path | App running, API returning categories | 1. Navigate to / 2. Wait for loading to finish 3. Check category cards | Category cards appear after skeleton disappears, count > 0 | — | Ready to Execute | High | API data display |
| TC-23 | Categories | Category cards have images and names | UI/UX | App running, categories loaded | 1. Navigate to / 2. Wait for categories 3. Check each card | Each card has icon and non-empty category name | — | Ready to Execute | Medium | Card content verification |
| TC-24 | Products | Featured products are loaded and displayed in grid | Happy Path | App running, API returning products | 1. Navigate to / 2. Wait for loading 3. Check products grid | Products grid visible with product cards, count > 0 | — | Ready to Execute | High | Product loading |
| TC-25 | Products | Product cards show image, name, price, rating, add to cart | UI/UX | App running, products loaded | 1. Navigate to / 2. Wait for products 3. Check first card elements | Card shows image, name text, price ($XX.XX), rating stars, Add to Cart button | — | Ready to Execute | High | Product card completeness |
| TC-26 | Products | Clicking "Add to Cart" shows toast notification | Happy Path | User logged in, products loaded | 1. Login user 2. Reload page 3. Click "Add" on first product | Toast notification appears with "added to cart" message | — | Ready to Execute | High | Add to cart flow |
| TC-27 | Products | Trending products section is visible with horizontal scroll | UI/UX | App running | 1. Navigate to / 2. Check trending section | Trending section visible with "Trending Now" title and left/right carousel buttons | — | Ready to Execute | Medium | Trending carousel |
| TC-28 | Promotional | Promotional banner is visible with discount text and CTA | UI/UX | App running | 1. Navigate to / 2. Check promo banner | Banner shows "Limited Time Offer" tag, "Up to 50% Off" title, "Shop Deals" button | — | Ready to Execute | Medium | Promotional content |
| TC-29 | Trust | Trust badges section shows 3 badges | UI/UX | App running | 1. Navigate to / 2. Check trust badges | 3 badges visible: Secure Payment, Easy Returns, Free Shipping | — | Ready to Execute | Medium | Trust indicators |
| TC-30 | Trust | Testimonials section shows customer reviews | UI/UX | App running | 1. Navigate to / 2. Check testimonials section | Section title visible, >= 3 testimonial cards with quotes and author names | — | Ready to Execute | Medium | Social proof |
| TC-31 | Newsletter | Newsletter form accepts email and shows success | Happy Path | App running | 1. Navigate to / 2. Enter valid email 3. Click Subscribe | Success feedback "Thanks for subscribing" displayed | — | Ready to Execute | High | Newsletter subscription |
| TC-32 | Newsletter | Newsletter shows error for invalid/duplicate email | Validation | App running | 1. Enter invalid email, submit 2. Enter valid email, subscribe 3. Reload, try same email | Error for invalid format; error for duplicate email | — | Ready to Execute | High | Email validation |
| TC-33 | Footer | Footer shows all 4 columns with links | UI/UX | App running | 1. Navigate to / 2. Scroll to footer 3. Check columns | 4 columns: Brand, Company (3 links), Support (3 links), Legal (3 links) | — | Ready to Execute | Medium | Footer structure |
| TC-34 | Footer | Footer shows payment method icons and copyright | UI/UX | App running | 1. Navigate to / 2. Check footer bottom | Copyright "© 2026 ShopEY", 4 payment icons (VISA, MC, PayPal, Amex) | — | Ready to Execute | Medium | Footer content |
| TC-35 | Responsive | Page is responsive — products go to 2 columns on tablet | Responsive | App running | 1. Set viewport 768x1024 2. Navigate to / 3. Check grid columns | Products grid shows <= 2 columns on tablet viewport | — | Ready to Execute | Medium | Tablet responsive |
| TC-36 | Responsive | Navbar collapses on mobile viewport | Responsive | App running | 1. Set viewport 375x667 2. Navigate to / 3. Check nav-links | Nav-links hidden, logo still visible | — | Ready to Execute | Medium | Mobile responsive |
| TC-37 | Cart Sidebar | Cart sidebar opens when cart icon clicked | UI/UX | App running | 1. Navigate to / 2. Click cart icon | Cart sidebar gains "open" class, "Your Cart" heading visible | — | Ready to Execute | High | Cart sidebar interaction |
| TC-38 | Cart Sidebar | Cart sidebar can be closed | UI/UX | App running, cart sidebar open | 1. Open cart sidebar 2. Click close button | Cart sidebar loses "open" class | — | Ready to Execute | High | Cart sidebar dismiss |

---

## Summary

- **Total Test Cases:** 38
- **Login Module:** 15 (TC-01 to TC-15)
- **Home Page:** 23 (TC-16 to TC-38)
- **Categories:** Happy Path (7), Validation (6), Error Handling (3), UI/UX (16), Navigation (4), Responsive (2)
- **Priority:** High (18), Medium (18), Low (2)
- **Status:** All Ready to Execute

## Execution Prerequisites

1. Docker containers running (`docker-compose up`)
2. Frontend accessible at `http://localhost:5173`
3. Backend accessible at `http://localhost:8000`
4. Database seeded and ready
5. Playwright installed (`cd tests/e2e && npm install && npx playwright install chromium`)

## Run Command

```bash
cd tests/e2e
npm install
npx playwright install chromium
npx playwright test
```
