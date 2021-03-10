# Travis
## Pre-requisites
`brew install travis` 
or as the [guide](https://docs.cloud.service.gov.uk/using_ci.html#assess-travis) says: `gem install travis --no-rdoc --no-ri`

# Steps to install Travis

1. I had to login to travisci and authorise the use
2. I had to run
`travis login --pro --github-token=<GENERATED_TOKEN_IN_GITLAB>`
3. I was currently not able to list the `wearesnook` github repo I created


# Configuration

## Include only the desired branches
```
# safelist
branches:
  only:
  - master
  - stable
  ```