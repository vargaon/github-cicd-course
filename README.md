# GitHub CI/CD practice

Sources for practice lecture about containers used in NSWI026 MFF UK and SEPA4M33SEP, FEL CVUT. This should be a simple example for CI/CD, it's not recommended for a production usage.

## Tasks

1. Take a look on basic usage of GitHub workflows.
    - https://docs.github.com/en/actions/examples/using-scripts-to-test-your-code-on-a-runner

2. Take a look on script in `task_a`.
    - (Optional) Prepare an env `python3 -m venv venv`, activate it `source venv/bin/activate` and install dependencies `pip3 install -r requirements.txt`.
    - (Optional) Try to execute tests `pytest task_a.py`.

### On push events

3. Make one test failing and fill a GitHub workflow to execute tests.
    - Change `.github/workflows/task-a-cd.yml` and push it to your GitHub.
4. Try to speed up testing using cache on one of following methods.
    - Using `cache: 'pip'` in [`actions/setup-python`](https://github.com/actions/setup-python?tab=readme-ov-file#caching-packages-dependencies)
    - Using [`actions/cache`](https://github.com/actions/cache)
5. Generate an html report with `--html=report.html` and upload it to GitHub using [`actions/upload-artifact`](https://github.com/actions/upload-artifact)
6. Run tests on multiple operating systems and Python versions using matrix option.
    ```yml
    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        os: [ubuntu-latest, macos-latest, windows-latest]
        python-version: ["3.10", "3.11", "pypy3.10"]
        exclude:
          - os: macos-latest
            python-version: "3.10"
          - os: windows-latest
            python-version: "3.10"
    ```

### On pull request

7. Change "task-a-cd.yml" to `task-a-ci.yml` and change to be executed on a pull-request, take a look on `pull_request`.
8. Run this pull request only on changes tu folder `task_a`, take a look on `paths`.

### On manual event

9. Try a manual workflow "task-b manual".
10. Build a docker image, using `docker/build-push-action`, you could reuse following lines
  - Create an workflow input `tag` for image tag
  - Tag image like ghcr.io/${{ github.repository }}:${{ inputs.tag }}
11. Build a dependent job `test`
  - It should depend on `docker` job
  - It should run docker container from previous step as [service container](https://docs.github.com/en/actions/using-containerized-services/about-service-containers)
  - Call `curl 127.0.0.1:8080/index.html` to fetch `index.html`

### Build our flight-log

12. Get own repository for FlightLog 
  - CI - Test application on pull-request
    - Java - `mvn test`
    - .NET - https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-net#building-and-testing-your-code
  - CD - Build a docker image on push to master / develop 
    - Java - https://spring.io/guides/topicals/spring-boot-docker/
    - .NET - https://learn.microsoft.com/en-us/dotnet/core/docker/build-container
