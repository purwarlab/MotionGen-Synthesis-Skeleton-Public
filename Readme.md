# Hi there! Thank you for your interest in MotionGen. 

This repository is a skeleton for the kinematic synthesis of mechanisms for our app. 

# Files and what they are saving: 

## 1. BSIdict_468_062324_3.json -> Saves all the kinematic structure matrices (B, S, I) for the following dataset paper: 

"A Dataset of 3M Single-DOF Planar 4-, 6-, and 8-Bar Linkage Mechanisms With Open and Closed Coupler Curves for Machine Learning-Driven Path Synthesis"

## 2. KV_468.json and VK_468.json -> key-value pair and value-key pair. 

We give one key to each mechanism type. Key is the string (e.g., 49), and value is the string ("RRRR")

## 3. datasetProcess.py 

MotionGen has sorted the mechanisms into four-bar, six-bar, and eight-bar. Feel free to use this sorted result.  

If you would like, you can write all your synthesis codes in this script. We split the synthesis code to decode (under main.py), and getMech (under datasetProcess.py). 

This can be redundant for your research. Feel free to change them. 

## 4. main.py 

The main function of the backend server. You will need to start a backend server to communicate with MotionGen. 


# Prerequisites: 

1. Python 3.7 or higher 

2. The libraries in requirements.txt (which you can install using <pip install -r requirements.txt>)


# How to use: 

To run the backend server locally, you can: 

1. Go to this directory. In the console, use <python main.py>

2. Open https://motiongen.io/core and press <ctrl + F2> to open panel. 

3. Under the text bar "Path Synthesis URL", change the link to your local server portal. 

    You may get the following messages in the console. For example, 

        * Serving Flask app 'main'
        * Debug mode: on
            WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
        * Running on all addresses (0.0.0.0)
        * Running on http://127.0.0.1:8080
        * Running on http://192.168.1.132:8080

    The link you want to paste would be 

        http://127.0.0.1:8080/image-based-path-synthesis

4. Open Path Synthesis. Draw any curve / path points, then press run. 

    The skeleton code, without any modification, will return an RRRR linkage mechanism. 


