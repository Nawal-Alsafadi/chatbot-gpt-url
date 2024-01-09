import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from api.models.chat_model.emix_service_model.emix_service_model import EmixServiceChat
from api.routes.app_routes import app_routes
from api.utils.first_init import FirstInit
from flask import Flask, jsonify, render_template
from flask_cors import CORS
import os
from importlib.metadata import version, PackageNotFoundError


firstInit = FirstInit()
# os.environ['LLAMA_INDEX_CACHE_DIR'] = 'A:/Work/vercel-Deployment/chatbot-emix-deploy/api/nltk_data'
# os.environ["OPENAI_API_KEY"] = str(firstInit.get_api_key())
os.environ.get('OPENAI_API_KEY')
app = Flask(__name__)
app.debug = True
CORS(app)   
app_routes(app)


def check_packages():
    packages_to_check = ["langchain==0.0.0", "llama_index==0.9.11", "flask==2.3.2", "flask_cors==3.0.10","pandas"]
    results = {}

    for package in packages_to_check:
        package_name, _, desired_version = package.partition("==")

        try:
            installed_version = version(package_name)
            if installed_version == desired_version:
                results[package] = "installed"
            else:
                results[package] = f"installed, but version {installed_version} instead of {desired_version}"
        except PackageNotFoundError:
            results[package] = "not installed"
    results['OPENAI_API_KEY'] = os.environ.get('OPENAI_API_KEY')

    return results

@app.route('/check_packages', methods=['GET'])
def route_check_packages():
    results = check_packages()
    return jsonify(results)

@app.route("/")
def hello_world():
    return render_template("index.html")

if __name__ == "__main__":
    # print("myPath" ,os.environ.get('LLAMA_INDEX_CACHE_DIR')  ) 

    app.run()
