class AddCustomer:
    #add customer page
    side_bar_link_id="nopSideBarPusher"
    customer_sidebar_link="//ul[@class='nav nav-pills nav-sidebar flex-column nav-legacy']/li[4]/a"
    customers_link="//ul[@class='nav nav-pills nav-sidebar flex-column nav-legacy']/li[4]/ul/li[1]/a"
    add_new_btn="//ul[@class='nav nav-pills nav-sidebar flex-column nav-legacy']/li[4]/ul/li[1]/a"
    email_input="//input[@id='Email']"
    password_input="//input[@id='Password']"
    first_name_input="//input[@id='FirstName']"
    last_name_input=" //input[@id='LastName']"
    gender_mail_input_radio="//input[@id='Gender_Male']"
    gender_female_input_radio="//input[@id='Gender_Female']"
    company_name_input="//input[@id='Company']"
    is_tax_attempt_input_check="//input[@id='IsTaxExempt']"
    newsletter_select="//div[@class=\'input-group-append\']//select[@id='SelectedNewsletterSubscriptionStoreIds']"
    customer_roles_select="//select[@id ='SelectedCustomerRoleIds']/option[@value = '1']"
    manager_vendor_select="//select[@id='VendorId']/option[@value='0']"
    active_check="//input[@id='Active']"
    admin_comment="//textarea[@id='AdminComment']"

    def __init__(self,driver):
        self.driver=driver



