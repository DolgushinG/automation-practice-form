import pytest

from constants import DATA_ROOT
from pages.StudentRegistrationFormPage import StudentRegistrationFormPage


@pytest.mark.usefixtures("driver")
class TestRegistrationForm:
    @pytest.mark.parametrize('first_name,last_name,email,phone, address, state, city',
                             [("IVAN", "IVANOV", "ivanov_ivan@gmail.com",
                               "9992095596", 'some address', 'NCR', 'Delhi')])
    def test_open_page(self, first_name, last_name, email, phone, address, state, city):
        student_reg_form = StudentRegistrationFormPage(self.driver)
        student_reg_form._go_to_url('https://demoqa.com/automation-practice-form')
        student_reg_form.fill_first_name(first_name)
        student_reg_form.fill_last_name(last_name)
        student_reg_form.fill_email(email)
        student_reg_form.click_checkbox_gender_male()
        student_reg_form.fill_mobile_phone(phone)
        student_reg_form.click_checkbox_hobbies_sports()
        file = DATA_ROOT + '/picture.png'
        student_reg_form.attach_picture(file)
        student_reg_form.fill_current_address(address)
        student_reg_form.remove_footer()
        student_reg_form.scroll_down()
        student_reg_form.select_state()
        student_reg_form.select_city()
        student_reg_form.scroll_down()
        student_reg_form.click_btn_submit()
        student_reg_form.verify_confirm_form()
        student_reg_form.verify_full_name(first_name, last_name)
        student_reg_form.verify_email(email)
        student_reg_form.verify_gender_male()
        student_reg_form.verify_mobile_phone(phone)
        student_reg_form.verify_checkbox_hobbies_sports()
        student_reg_form.verify_picture()
        student_reg_form.verify_current_address(address)
        student_reg_form.verify_state_and_city(state, city)
