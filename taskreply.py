import pytest 
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
 
@pytest.fixture(scope="module") 
def driver(): 
    service = Service("chromedriver.exe") 
    options = webdriver.ChromeOptions() 
    driver = webdriver.Chrome(service=service, options=options) 
    driver.maximize_window() 
    driver.get("https://userinyerface.com/game.html") 
    yield driver 
    driver.quit() 
 
def test_cookies_div_icon_logo(driver): 
    wait = WebDriverWait(driver, 10)  # Define WebDriverWait object
    eleCookiesDiv2 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.logo__icon'))) 
 
    background_color = eleCookiesDiv2.value_of_css_property("background-color") 
    font_family = eleCookiesDiv2.value_of_css_property("font-family") 
    color = eleCookiesDiv2.value_of_css_property("color") 
    font_size = eleCookiesDiv2.value_of_css_property("font-size") 
    font_weight = eleCookiesDiv2.value_of_css_property("font-weight") 
    background_image = eleCookiesDiv2.value_of_css_property("background-image") 
    background_size = eleCookiesDiv2.value_of_css_property("background-size") 
    background_position = eleCookiesDiv2.value_of_css_property("background-position") 
    background_repeat = eleCookiesDiv2.value_of_css_property("background-repeat") 
    width = eleCookiesDiv2.value_of_css_property("width") 
    height = eleCookiesDiv2.value_of_css_property("height") 
    display = eleCookiesDiv2.value_of_css_property("display") 
 
    assert background_color == "rgba(255, 255, 255, 1)", f"Expected background color rgba(255, 255, 255, 1), but got {background_color}" 
    assert font_family == "Poppins, sans-serif", f"Expected font family 'Poppins, sans-serif', but got {font_family}" 
    assert color == "rgba(255, 255, 255, 1)", f"Expected color rgba(255, 255, 255, 1), but got {color}" 
    assert font_size == "40px", f"Expected font size 40px, but got {font_size}" 
    assert font_weight == "700", f"Expected font weight 700, but got {font_weight}" 
    assert background_image == "url(\"https://userinyerface.com/images/userinyerface-logo.svg\")", f"Expected background image URL, but got {background_image}" 
    assert background_size == "contain", f"Expected background size 'contain', but got {background_size}" 
    assert background_position == "center", f"Expected background position 'center', but got {background_position}" 
    assert background_repeat == "no-repeat", f"Expected background repeat 'no-repeat', but got {background_repeat}" 
    assert width == "300px", f"Expected width '300px', but got {width}" 
    assert height == "175px", f"Expected height '175px', but got {height}" 
    assert display == "inline-block", f"Expected display 'inline-block', but got {display}" 
 
def test_cookies_div_properties(driver): 
    wait = WebDriverWait(driver, 10)  # Define WebDriverWait object
    eleCookiesDiv = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.cookies'))) 
 
    background_color = eleCookiesDiv.value_of_css_property("background-color") 
    width = eleCookiesDiv.value_of_css_property("width") 
    height = float(eleCookiesDiv.size['height'])  # Convert height to float 
 
    assert background_color == "rgba(255, 0, 0, 1)", "Background color is not as expected" 
    assert height == 155.2, "Height is not as expected" 
 
    width_value = float(width.rstrip('px')) 
    assert width_value == 300, "Width is not as expected" 
    assert height == 175, "Height is not as expected" 

def test_cookies_div_password(driver): 
    wait = WebDriverWait(driver, 10)  
    eleCookiesDiv3 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.login-form__container'))) 
 
    height = float(eleCookiesDiv3.size['height']) 
    width = float(eleCookiesDiv3.size['width']) 
    background_color = eleCookiesDiv3.value_of_css_property("background-color") 
    box_shadow = eleCookiesDiv3.value_of_css_property("box-shadow") 
    border_radius = eleCookiesDiv3.value_of_css_property("border-radius") 
    position = eleCookiesDiv3.value_of_css_property("position") 
    left = eleCookiesDiv3.value_of_css_property("left") 
    top = eleCookiesDiv3.value_of_css_property("top") 
    box_sizing = eleCookiesDiv3.value_of_css_property("box-sizing") 
    padding = eleCookiesDiv3.value_of_css_property("padding") 
 
    assert height == 297, f"Expected height 297px, but got {height}px" 
    assert width == 436, f"Expected width 436px, but got {width}px" 
    assert background_color == "rgb(255, 255, 255)", "Background color is not as expected" 
    assert box_shadow == "rgba(0, 0, 0, 0.08) 0px 0px 7px 0px", "Box shadow is not as expected" 
    assert border_radius == "8px", "Border radius is not as expected" 
    assert position == "absolute", "Position is not as expected" 
    assert left == "0px", "Left position is not as expected" 
    assert top == "0px", "Top position is not as expected" 
    assert box_sizing == "border-box", "Box sizing is not as expected" 
    assert padding == "32px", "Padding is not as expected" 

if __name__ == "__main__": 
    pytest.main()
