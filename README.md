# Backend for FAQ Application using Django

## Installation steps
### Python setup
1. Fork and Clone the repository.
    Go to the GitHub repository page.
    Click Fork to create a copy of the repository in your account.
    Clone the forked repository to your local system using:
    git clone https://github.com/Aniket6207/django-multilanguage-faq
   
2. Install python. (This application is developed in 3.10.1 so this version is preferred.) ([Link](https://www.python.org/downloads/))
   
3. Install pip and upgrade it to latest version. (Refer to [Link](https://ultahost.com/knowledge-base/how-to-install-and-upgrade-pip-to-the-latest-version/))

4. Create a virtual environment and activate it. (Refer to [Link](https://www.geeksforgeeks.org/python-virtual-environment/))

5. Install required libraries mentioned in requirements.txt using below command (cd to the directory where requirements.txt is located)<br/>
   pip install -r requirements.txt

### Docker setup
1. Install docker (Refer to [Docker Official website](https://docs.docker.com/engine/install/))
   
2. As we are using Redis for caching, we need to pull its docker image. To do so - <br/>
   Run this command : **"docker run --name django-redis -d -p 6379:6379 --rm redis"** <br/>
   ( Make sure docker hub is running)

 ### Starting Web server
 1. Without using docker<br/>
    Use below command: <br/>
    **python manage.py runserver**
    
 2. Using Docker
    Run below commands <br/>
    **docker compose build** <br/>
    **docker compose up** <br/>

## API Documentation
1. **/api/faq/**
   - Support langauge selection **?lang=en**
   - Example  **curl http://localhost:8000/api/faqs/** 
   - Output 
     ![image](https://github.com/user-attachments/assets/ce8feb6c-471b-4358-8a19-dc19ec047c29)

   - Example  **curl http://localhost:8000/api/faqs/?lang=bn**
   - Output
     ![image](https://github.com/user-attachments/assets/ef79eeb8-ece6-4efd-826d-8c9054ec9f3a)
   - When passed no parameter or invalid langauge, the FAQs are provided in English (Default Language)
  

2. **/admin**
   - Admin Page
   - Use below test credentials to login<br/>
     Username - test_admin<br/>
     Password - Testpassword

## Contribution Guidelines
  1. Code Style: Ensure code follows the project's formatting rules.
  2. Testing: Add tests for new features or changes. Ensure all tests pass before submitting a PR.
  3. Documentation: Update or add documentation as needed.
  4. Issue Reporting:<br/>
      Search existing issues before creating a new one.<br/>
      Provide detailed information, including steps to reproduce the issue.<br/>


<br/><br/>
📫 How to reach me **aniketmore6207@gmail.com**

<h3 align="left">Connect with me:</h3>
<p align="left">
<a href="https://twitter.com/an1ket_more" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/twitter.svg" alt="an1ket_more" height="30" width="40" /></a>
<a href="https://www.youtube.com/@aniketmore8789" target="blank"><img align="center" src="https://upload.wikimedia.org/wikipedia/commons/4/42/YouTube_icon_%282013-2017%29.png" alt="aniket_1711" height="30" width="40" /></a>
<a href="https://codeforces.com/profile/an1ket_62" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/codeforces.svg" alt="an1ket_62" height="30" width="40" /></a>
