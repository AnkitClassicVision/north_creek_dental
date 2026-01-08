# Website Creation Prompt

## Instructions

Create a website in the folder `/website` following these guidelines:

### Content & Structure
- Follow the directions in `website_map_master_template_old.md` for:
  - Website structure and page organization
  - Content mapping and information architecture
  - Persona cards, competitive analysis, funnels, marketing, partnerships sections
  - Data formatting and calculation methodologies
  - Persona images location: `/RESEARCH/images/` (copy to `/website/assets/images/personas/`)

### Data Sources
- Use `/RESEARCH` folder for research data and content
- Use `New_question_dynamic.md` for understanding the research methodology
- **Company Logo**: Extract from the company website URL specified in `New_question_dynamic.md` (under `company.website`)
  - Save to `/RESEARCH/images/[COMPANY_SHORTNAME]_logo.png`
  - Copy to `/website/assets/images/[COMPANY_SHORTNAME]_logo.png`
  - Use in website header/navigation and footer

### Visual Design System
- **IMPORTANT**: Apply the "Ethereal Clarity" design system from `deisgn_elements.txt`

#### Core Design Elements
- **Glass Cards**: Frosted glassmorphism effect with backdrop blur
- **Aurora Background**: Animated colored blobs (Soft Indigo, Rose, Teal) moving slowly
- **Typography**: Playfair Display for headings, Inter for body/UI
- **Colors**: Tinted neutrals (no pure black/white), Slate palette
- **Animations**: Hover lift effects, spotlight on cursor, scroll reveal
- **Whitespace**: Generous padding (2x normal)
- **Buttons**: Pill-shaped with subtle shadows

#### Icons & Imagery (CRITICAL)
- **NO EMOJIS**: Standard emojis are strictly forbidden - they clash with premium aesthetic
- **Use Lucide Icons**: High-quality, thin-stroke SVG icons (stroke-width: 1.5px)
- **Icon Colors**: Inherit text color or use Primary Accent (#6366F1) for emphasis
- **Icon Containers**: Place key icons inside "Glass Squircle" (rounded square) with soft colored background (e.g., bg-indigo-50)

#### Persona Images
- Shape: Circular crops with `border-radius: 50%`
- Border: 3px solid white (#FFFFFF) border
- Shadow: Soft shadow to pop off glass cards
- Style: High-quality color headshots with soft lighting preferred

#### Data Visualization (if applicable)
- Lines: Use gradients (e.g., Emerald fading to transparent), not solid colors
- Grid Lines: Dotted and extremely subtle (rgba(0,0,0,0.05))
- Tooltips: Glassmorphism style (blurred background) instead of solid black boxes

### Execution
1. Plan the implementation first
2. Create/update all HTML pages maintaining the same structure and navigation
3. Apply the Ethereal Clarity design system throughout
4. Replace ALL emojis with Lucide SVG icons
5. Ensure persona headshot images are properly integrated with white border styling
6. Test all navigation links work correctly

### Post-Creation Review (CRITICAL - Ultrathink Mode)
**After completing the website, perform a comprehensive review of EACH page using extended thinking.**

```yaml
review_checklist:
  design_compliance:
    - [ ] Aurora background present and animating on all pages
    - [ ] Glass cards using proper glassmorphism (backdrop-blur, gradient bg, white border)
    - [ ] Typography: Playfair Display for headings, Inter for body text
    - [ ] Colors: No pure black (#000) or pure white (#FFF) - use Slate palette
    - [ ] Icons: ALL Lucide SVG icons, NO emojis anywhere
    - [ ] Icon containers: Glass squircle styling where appropriate
    - [ ] Buttons: Pill-shaped with subtle shadows
    - [ ] Whitespace: Generous padding throughout
    - [ ] Hover effects: Lift animations on cards, spotlight effect
    - [ ] Scroll reveal: Elements fade in on scroll

  data_accuracy:
    - [ ] All research data properly mapped from /RESEARCH folder
    - [ ] Persona information complete (name, age, demographics, pain points, etc.)
    - [ ] Competitive analysis data accurate and complete
    - [ ] Funnel stages and metrics correctly displayed
    - [ ] Marketing strategies aligned with research findings
    - [ ] Partnership opportunities accurately represented
    - [ ] Executive summary reflects all key findings

  visual_appeal:
    - [ ] Consistent visual hierarchy across all pages
    - [ ] Card layouts balanced and aligned
    - [ ] Images properly sized and positioned
    - [ ] Persona headshots: circular, 3px white border, soft shadow
    - [ ] Company logo properly placed in header/footer
    - [ ] Color harmony maintained (no clashing colors)
    - [ ] Responsive considerations addressed
    - [ ] No broken layouts or overflow issues

  navigation_integrity:
    - [ ] All nav links functional and pointing to correct pages
    - [ ] Active page indicator working
    - [ ] Consistent navigation across all pages
    - [ ] Footer links working

  page_by_page_review:
    - index.html (Home/Landing)
    - executive-summary.html
    - personas.html
    - competitive.html
    - funnels.html
    - marketing.html
    - partnerships.html

review_process:
  1. Open each page individually
  2. Check against design_elements.txt specifications
  3. Verify data matches research documents
  4. Assess visual appeal and consistency
  5. Document any issues found
  6. Fix all issues before marking complete
```

---

### Performance Optimization Requirements (CRITICAL)

**Target Metrics (Core Web Vitals):**
- LCP (Largest Contentful Paint): < 2.5 seconds
- FID (First Input Delay): < 100ms
- CLS (Cumulative Layout Shift): < 0.1
- Total page weight: < 1.5MB

#### 1. Critical Rendering Path

```html
<!-- In <head>: Inline critical CSS for above-fold content -->
<style>
  :root {
    --color-indigo: #6366f1;
    --color-rose: #f43f5e;
    --color-teal: #14b8a6;
    --color-slate-900: #0f172a;
  }
  body {
    margin: 0;
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    background: var(--color-slate-900);
  }
  .aurora-bg { position: fixed; inset: 0; overflow: hidden; z-index: -1; }
  .hero { min-height: 100vh; display: flex; align-items: center; justify-content: center; }
</style>

<!-- Defer non-critical CSS -->
<link rel="preload" href="./assets/css/main.css" as="style" onload="this.onload=null;this.rel='stylesheet'">
<noscript><link rel="stylesheet" href="./assets/css/main.css"></noscript>

<!-- Defer non-critical JavaScript -->
<script defer src="./assets/js/main.js"></script>
```

#### 2. Font Loading Strategy

```html
<!-- ALWAYS include these preconnect hints in <head> -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>

<!-- Load fonts with display=swap -->
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Playfair+Display:wght@500;600;700&display=swap" rel="stylesheet">
```

```css
/* Font fallback stacks - always include */
body {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
}
h1, h2, h3, h4, h5, h6 {
  font-family: 'Playfair Display', Georgia, 'Times New Roman', serif;
}
```

#### 3. Image Requirements

**Mandatory attributes:**
- ALL images MUST have `width` and `height` attributes (prevents CLS)
- Below-fold images: `loading="lazy" decoding="async"`
- Hero/above-fold images: `loading="eager" fetchpriority="high"`
- Max persona image size: 50KB each

```html
<!-- Hero image template (above fold) -->
<img
  src="./assets/images/hero.webp"
  alt="Description"
  width="400" height="400"
  loading="eager"
  fetchpriority="high"
>

<!-- Below-fold image template with WebP + fallback -->
<picture>
  <source type="image/webp" srcset="./assets/images/persona.webp">
  <img
    src="./assets/images/persona.jpg"
    alt="Persona Name"
    width="200" height="200"
    loading="lazy"
    decoding="async"
    class="persona-img"
  >
</picture>
```

#### 4. Aurora Background - GPU Optimized (REQUIRED)

```css
/* Aurora blobs MUST use transform3d for GPU acceleration */
.aurora-blob {
  position: absolute;
  border-radius: 50%;
  filter: blur(80px);
  opacity: 0.6;
  will-change: transform;
  transform: translate3d(0, 0, 0);
  animation: aurora-float 20s ease-in-out infinite;
}

.aurora-blob--indigo {
  width: 40vw; height: 40vw;
  background: radial-gradient(circle, var(--color-indigo) 0%, transparent 70%);
  left: 10%; top: 20%;
}

.aurora-blob--rose {
  width: 35vw; height: 35vw;
  background: radial-gradient(circle, var(--color-rose) 0%, transparent 70%);
  right: 15%; top: 30%;
  animation-delay: -7s;
}

.aurora-blob--teal {
  width: 30vw; height: 30vw;
  background: radial-gradient(circle, var(--color-teal) 0%, transparent 70%);
  left: 40%; bottom: 20%;
  animation-delay: -14s;
}

/* ONLY use transform for animation - never top/left/width/height */
@keyframes aurora-float {
  0%, 100% { transform: translate3d(0, 0, 0) scale(1); }
  25% { transform: translate3d(5%, -3%, 0) scale(1.05); }
  50% { transform: translate3d(-3%, 5%, 0) scale(0.95); }
  75% { transform: translate3d(-5%, -2%, 0) scale(1.02); }
}

/* REQUIRED: Reduced motion support for accessibility */
@media (prefers-reduced-motion: reduce) {
  .aurora-blob {
    animation: none;
    will-change: auto;
  }
}
```

#### 5. Glassmorphism - Performance Limits

**CRITICAL: Limit `backdrop-filter: blur()` to maximum 5 elements per page**

```css
.glass-card {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 16px;
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  isolation: isolate; /* Prevents repaint propagation */
  transition: transform 0.3s ease, opacity 0.3s ease;
}

/* Apply will-change ONLY on hover */
.glass-card:hover {
  will-change: transform;
  transform: translateY(-4px);
}

.glass-card:not(:hover) {
  will-change: auto;
}

/* REQUIRED: Fallback for unsupported browsers */
@supports not (backdrop-filter: blur(12px)) {
  .glass-card {
    background: rgba(20, 20, 30, 0.9);
  }
}

/* Reduced motion fallback */
@media (prefers-reduced-motion: reduce) {
  .glass-card {
    backdrop-filter: none;
    background: rgba(20, 20, 30, 0.85);
  }
  .glass-card:hover {
    transform: none;
  }
}
```

#### 6. Resource Loading - Lazy Load Effects

```javascript
// Lazy load scroll reveal effects
document.addEventListener('DOMContentLoaded', () => {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('revealed');
        observer.unobserve(entry.target);
      }
    });
  }, { rootMargin: '50px', threshold: 0.1 });

  document.querySelectorAll('[data-reveal]').forEach(el => observer.observe(el));
});

// Lazy load spotlight cursor effect on first interaction
let spotlightLoaded = false;
function loadSpotlight() {
  if (spotlightLoaded) return;
  spotlightLoaded = true;
  // Initialize spotlight effect here
}
document.addEventListener('mousemove', loadSpotlight, { once: true });
```

#### 7. SVG Icon Sprite Template

```html
<!-- Include once at top of body - hidden sprite sheet -->
<svg style="display: none;">
  <symbol id="icon-arrow-right" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
    <path d="M5 12h14M12 5l7 7-7 7"/>
  </symbol>
  <symbol id="icon-check" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
    <path d="M20 6L9 17l-5-5"/>
  </symbol>
  <symbol id="icon-users" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
    <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/>
    <circle cx="9" cy="7" r="4"/>
    <path d="M23 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75"/>
  </symbol>
  <!-- Add more icons as needed -->
</svg>

<!-- Usage throughout page -->
<svg class="icon" width="24" height="24"><use href="#icon-arrow-right"/></svg>
```

### Performance Checklist (Verify Before Complete)

```yaml
performance_validation:
  critical_path:
    - [ ] Critical CSS inlined in <head>
    - [ ] Non-critical CSS uses preload pattern
    - [ ] Scripts use defer attribute

  fonts:
    - [ ] Preconnect hints for fonts.googleapis.com and fonts.gstatic.com
    - [ ] font-display: swap in use
    - [ ] System font fallbacks defined

  images:
    - [ ] ALL images have width and height attributes
    - [ ] Hero images use loading="eager" fetchpriority="high"
    - [ ] Below-fold images use loading="lazy"
    - [ ] Persona images < 50KB each

  animations:
    - [ ] Aurora uses transform3d (NOT top/left)
    - [ ] will-change only on :hover, not globally
    - [ ] @media (prefers-reduced-motion) rules present

  glassmorphism:
    - [ ] backdrop-filter used on MAX 5 elements
    - [ ] @supports fallback for unsupported browsers
    - [ ] isolation: isolate on glass cards

  lazy_loading:
    - [ ] Scroll reveal uses IntersectionObserver
    - [ ] Spotlight effect lazy loads on interaction
    - [ ] SVG sprite for repeated icons
```
