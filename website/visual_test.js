const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();

  // Set desktop viewport
  await page.setViewportSize({ width: 1920, height: 1080 });

  console.log('Capturing screenshots for NCDental Growth Dashboard...\n');

  // 1. Landing Page (index.html)
  console.log('1. Capturing landing page (index.html)...');
  await page.goto('http://localhost:8765/index.html');
  await page.waitForLoadState('networkidle');
  // Wait for animations to complete
  await page.waitForTimeout(2000);
  await page.screenshot({ path: '/mnt/d_drive/repos/north_creek_dental/website/screenshot_index_fullpage.png', fullPage: true });
  await page.screenshot({ path: '/mnt/d_drive/repos/north_creek_dental/website/screenshot_index_hero.png' });
  console.log('   - Full page screenshot saved: screenshot_index_fullpage.png');
  console.log('   - Hero section screenshot saved: screenshot_index_hero.png');

  // 2. Personas Page (personas.html)
  console.log('\n2. Capturing personas page (personas.html)...');
  await page.goto('http://localhost:8765/personas.html');
  await page.waitForLoadState('networkidle');
  await page.waitForTimeout(2000);
  await page.screenshot({ path: '/mnt/d_drive/repos/north_creek_dental/website/screenshot_personas_fullpage.png', fullPage: true });
  await page.screenshot({ path: '/mnt/d_drive/repos/north_creek_dental/website/screenshot_personas_hero.png' });
  console.log('   - Full page screenshot saved: screenshot_personas_fullpage.png');
  console.log('   - Hero section screenshot saved: screenshot_personas_hero.png');

  // 3. Click on Cosmetic tab to verify tab functionality
  console.log('\n3. Capturing cosmetic personas tab...');
  try {
    const cosmeticTab = page.locator('.tabs__tab:has-text("Cosmetic")');
    await cosmeticTab.click({ timeout: 5000 });
    await page.waitForTimeout(800);
    await page.screenshot({ path: '/mnt/d_drive/repos/north_creek_dental/website/screenshot_personas_cosmetic_tab.png', fullPage: true });
    console.log('   - Cosmetic tab screenshot saved: screenshot_personas_cosmetic_tab.png');
  } catch (e) {
    console.log('   - Tab click failed, capturing current state');
    await page.screenshot({ path: '/mnt/d_drive/repos/north_creek_dental/website/screenshot_personas_cosmetic_tab.png', fullPage: true });
  }

  // 4. Mobile viewport test (375x667)
  console.log('\n4. Capturing mobile viewport (375x667)...');
  await page.setViewportSize({ width: 375, height: 667 });
  await page.goto('http://localhost:8765/index.html');
  await page.waitForLoadState('networkidle');
  await page.waitForTimeout(1500);
  await page.screenshot({ path: '/mnt/d_drive/repos/north_creek_dental/website/screenshot_index_mobile.png', fullPage: true });
  console.log('   - Mobile screenshot saved: screenshot_index_mobile.png');

  await browser.close();
  console.log('\nAll screenshots captured successfully!');
})();
