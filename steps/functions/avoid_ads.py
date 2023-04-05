def click_avoid_ads(browser, element):
    element.click()
    if "#google_vignette" in browser.current_url:
        browser.back()
        element.click()