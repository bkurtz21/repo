# INSTRUCTIONS FOR USER TARGETING FEATURE FLAG SETUP #

In this guide, you will:
- Clone a sample web app from Glitch.com
- Add the LaunchDarkly SDK to the web app
- Create A User-Targeted Feature Flag for Pricing on your web app
- Turn on feature

Prerequisites
1) An active LaunchDarkly account
2) Access to Glitch.com account



# Setting up your Glitch Web App #

1. First step is to login into your Glitch.com account.

2. After you have signed in, you will need to clone the sample web app from Glitch.com 
that will create an editable copy of the Python web app. 

3. Visit https://glitch.com/edit/#!/remix/ld-space-camp-0
- This link will automatically clone the python web app into your Glitch account


# Setting up your LaunchDarkly project and SDK #

1. Navigate to Account Settings Page
2. Create new project or use exsisting one
3. In the Account Settings page, click to copy the SDK key to your clipboard

# Configuring the SDK key in your web app #
1. Click the .env file 
2. Assign the SDK Key you copied above to the variable LD_SDK_KEY:(YOUR-KEY)


# Install Python SDK #
1. Click the requirements file, and add LaunchDarkly Python SDK as a dependency to the app
2. Assign "launch-darkly-server-sdk" into the first line of the file

# Initialize LaunchDarkly #
1. After you install the Python SDK into requirements, you can now initialize it in the server.py file
2. Click server.py and add the following line "import ldclient"
3. Next, specifiy your SDK key to connect to LaunchDarkly by using 

         ldclient.set_sdk_key(os.getenv('LD_SDK_KEY'))

4. Additionally, add 

        ld_client = ldclient.get()
  
# Create Feature Flag in LaunchDarkly #

1. Click Feature Flags when signed into LaunchDarkly
2. Click +Flag
3. Enter name for feature flag
4. Leave flag variation set to Boolean
6. Save flag


# Add Routing for Feature Flag in Pricing Page #

1. Navigate to server.py file in Glitch folder
2. Designate route to handler by adding following code

        @app.route('/')
        def pricing():
        """Displays the pricing page."""
  
          user {
          "key": "anon",
          "anonymous": True
              }
  
            is_tier_3_enabled = ld_client.variation('pricing-tier-3', user, False)
            return render_template('pricing.html', is_tier_3_enabled=is_tier_3_enabled)` 
    
3. The evaluated feature flag  is (is_tier_3_enabled)

# Update Pricing Page to show new pricing tier based on Feature Flag #

1. Navigate to views/pricing.html
2. Update your template to look like this

        {% extends "base.html" %}
        {% block main %}
        <section class="pricing py-5">
          <div class="container">
          <div class="row justify-content-center">
            <div class="card-group">

              {% include "tier_1.html" %}
              {% include "tier_2.html" %}

                {# Tier 3 is now controlled by a feature flag! #}
                {% if is_tier_3_enabled == True %}
                    {% include "tier_3.html" %}
                    {% endif %}

            </div>
          </div>
        </div>
        </section>
        {% endblock %}

# Turn on Feature Flag within Web App #
1. Navigate to LaunchDarkly account and your recently created Flag 
2. Click the Targeting toggle to togle the flag to on
3. Enter a comment
4. Click Turn On
5. Refresh the browser, and verify that the new pricing tier is available and shown
