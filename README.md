# Creating an application with a Python code sample


## Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## Run Application
This will offer to forward port and open link in new tab
```bash
flask --app app.py --debug run
```

## Link Github 
* Setup Fine-grained personal access tokens https://github.com/settings/tokens?type=beta
* Open Terminal in Dev Spaces (top right corner logo with bottom pane)
* ```git config --global user.email "<your email>"```
* ```git config --global user.name "<your full name>"```
* ```git config credential.helper store```
* ```git push```
  * provide username
  * provide password

## Learn how to use Dev Spaces
**Note:** The Python code sample uses the **8081** HTTP port.

Before you begin creating an application with this `devfile` code sample, it's helpful to understand the relationship between the `devfile` and `Dockerfile` and how they contribute to your build. You can find these files at the following URLs:

* [Python `devfile.yaml`](https://github.com/devfile-samples/devfile-sample-python-basic/blob/main/devfile.yaml)
* [Python `Dockerfile`](https://github.com/devfile-samples/devfile-sample-python-basic/blob/main/docker/Dockerfile)

1. The `devfile.yaml` file has an [`image-build` component](https://github.com/devfile-samples/devfile-sample-python-basic/blob/main/devfile.yaml#L24-L30) that points to your `Dockerfile`.
2. The [`docker/Dockerfile`](https://github.com/devfile-samples/devfile-sample-python-basic/blob/main/docker/Dockerfile) contains the instructions you need to build the code sample as a container image.
3. The `devfile.yaml` [`kubernetes-deploy` component](https://github.com/devfile-samples/devfile-sample-python-basic/blob/main/devfile.yaml#L31-L43) points to a `deploy.yaml` file that contains instructions for deploying the built container image.
4. The `devfile.yaml` [`deploy` command](https://github.com/devfile-samples/devfile-sample-python-basic/blob/main/devfile.yaml#L51-L59) completes the [outerloop](https://devfile.io/docs/2.2.0/innerloop-vs-outerloop) deployment phase by pointing to the `image-build` and `kubernetes-deploy` components to create your application.

### Additional resources
* For more information about Python, see [Python](https://www.python.org/).
* For more information about devfiles, see [Devfile.io](https://devfile.io/).
* For more information about Dockerfiles, see [Dockerfile reference](https://docs.docker.com/engine/reference/builder/).
