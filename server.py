
import ldclient
import os
from flask import Flask, render_template

ldclient.set_sdk_key(os.getenv('LD_SDK_KEY'))

ld_client = ldclient.get()

app = Flask(__name__, static_folder='public', template_folder='views')

@app.route('/')
def pricing():
    """Displays the pricing page."""

    user = {
      "key": "anon",
      "anonymous": True
    }
    is_tier_3_enabled = ld_client.variation('pricing-tier-3', user, False)
    return render_template('pricing.html', is_tier_3_enabled=is_tier_3_enabled)

  
if __name__ == '__main__':
    app.run()

    