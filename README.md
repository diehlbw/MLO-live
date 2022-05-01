# Sentiment Analysis webapp prototype
## Usage
Currently the app uses FastAPI but has no real front-end. We make use of generated swagger docs to focus on functionality and Ops.
This project is an "work in progress" as class introduces further complexity to add to it; see week specific details for how to deploy.  

‼ Not guaranteed to be backwards compatible, so see tags (dates prior to Week4) in GitLab if you *really* want old functionality.

Once the server is up (depending on the week's detailed instructions):
1. Use your favorite browser to navigate to `<publicIP>:8080/docs`
0. Use the `/analyze` endpoint and "Try it out" for example sentiment analysis
   * Update the value for `query_string`
   * View score and label for results


## Week 4 - containerization
Once server is up and running, see usage above
### Option 1. Local deployment (ECR access)
1. From a prompt, it can be pulled and spun up in a single command:  
  `docker run -itp 8080:8080 public.ecr.aws/d4e8a7g0/bwd/mlo-live:wk4`
    * This includes running with -it vs -d to view live logging

### Option 2. Local deployment with local image build
If you don't have access to the ECR you need to build this locally:
1. Clone this repository and navigate to the project root
2. From a prompt run:  
  `$ docker build -t bwd-sentiment:local`  
  `$ docker run -p 8080:8080 bwd-sentiment:local`


## Week 3 - local venv
<details><summary>Old Instructions</summary>

The following may already be available via 44.201.231.8, but somewhat unlikely that the app is still running...

### Manual pre-setup, from project root:
This avoids anaconda because there is too much bloat for the micro EC2 instance to have room for that AND the  (sometimes) actually required torch/transformers libraries. 
Instructions will vary slightly depending on OS and python distribution

From the root of the cloned repository run the following:
1. `$ python3 -m venv env`  
1. `$ source env/bin/activate`  
1. `$ pip install -r src/requirements.txt`

### Actually spin up:
From inside the src directory
1. `$ uvicorn main:app --host 0.0.0.0 --port 8080`
</details>