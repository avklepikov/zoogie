# Contributing to Zoogie

First off, thanks for taking the time to contribute!

The following is a set of guidelines for contributing to Zoogie, which is hosted in the [ZoogieProject Organization](https://github.com/ZoogieProject) on GitHub. These are mostly guidelines, not rules. Use your best judgment, and feel free to propose changes to this document in a pull request.

---

#### Table Of Contents

[Code of Conduct](#code-of-conduct)

[I don't want to read this whole thing, I just have a question!!!](#i-dont-want-to-read-this-whole-thing-i-just-have-a-question)

[How Can I Contribute?](#how-can-i-contribute)
  * [Reporting Bugs](#reporting-bugs)
  * [Suggesting Enhancements](#suggesting-enhancements)
  * [Your First Code Contribution](#your-first-code-contribution)
  * [Pull Requests](#pull-requests)

[Styleguides](#styleguides)
  * [Git Commit Messages](#git-commit-messages)
  * [Documentation Styleguide](#documentation-styleguide)

[Additional Notes](#additional-notes)
  * [Issue and Pull Request Labels](#issue-and-pull-request-labels)

---

## Code of Conduct

This project and everyone participating in it is governed by the [Zoogie Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior to [support@zoogieproject.com](mailto:support@zoogieproject.com).

## I don't want to read this whole thing I just have a question!!!

> **Note:** Please don't file an issue to ask a question.

Please send your questions or suggestions to [support@zoogieproject.com](mailto:support@zoogieproject.com).

Official ZoogieProject web site `is currently under development`. Once it is working please visit it for: 
* Official Zoogie message board
* Forum
* Zoogie FAQ

If chat is more your speed, you can join the Slack team:

* [Join the ZoogieProject Slack Team](https://zoogieproject.slack.com/)
    * Even though Slack is a chat service, sometimes it takes several hours for community members to respond &mdash; please be patient!


## How Can I Contribute?

### Reporting Bugs

Feel free to send information about identified bug to [support@zoogieproject.com](mailto:support@zoogieproject.com) or raise an Issue at GitHub with label *Bug*.

> **Note:** If you find a **Closed** issue that seems like it is the same thing that you're experiencing, open a new issue and include a link to the original issue in the body of your new one.


### Suggesting Enhancements

This section guides you through submitting an enhancement suggestion for Zoogie, including completely new features and minor improvements to existing functionality. Following these guidelines helps maintainers and the community understand your suggestion :pencil: and find related suggestions :mag_right:.


### Your First Code Contribution

Unsure where to begin contributing to Zoogie? You can start by looking through these `beginner` and `help-wanted` issues:

* `beginner` - issues which should only require a few lines of code, and a test or two.
* `Help wanted issues` - issues which should be a bit more involved than `beginner` issues.



### Pull Requests
> **Section is under is under construction**


## Styleguides

### Git Commit Messages

* Use the present tense ("Add feature" not "Added feature")
* Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
* Limit the first line to 72 characters or less
* Reference issues and pull requests liberally after the first line
* When only changing documentation, include `[ci skip]` in the commit title
* Consider starting the commit message with an applicable emoji:
    * :art: `:art:` when improving the format/structure of the code
    * :racehorse: `:racehorse:` when improving performance
    * :memo: `:memo:` when writing docs
    * :penguin: `:penguin:` when fixing something on Linux
    * :apple: `:apple:` when fixing something on macOS
    * :checkered_flag: `:checkered_flag:` when fixing something on Windows
    * :bug: `:bug:` when fixing a bug
    * :fire: `:fire:` when removing code or files
    * :white_check_mark: `:white_check_mark:` when adding tests
    * :lock: `:lock:` when dealing with security
    * :arrow_up: `:arrow_up:` when upgrading dependencies
    * :arrow_down: `:arrow_down:` when downgrading dependencies

### Python Styleguide

> **Section is under is under construction**


### Documentation Styleguide

* Use [reStructuredText](https://docutils.sourceforge.io/rst.html) for Python code docstrings.
* Use [Markdown](https://daringfireball.net/projects/markdown) for general documentation on GitHub.




## Additional Notes

### Issue and Pull Request Labels

This section lists the labels we use to help us track and manage issues and pull requests. 

[GitHub search](https://help.github.com/articles/searching-issues/) makes it easy to use labels for finding groups of issues or pull requests you're interested in. We  encourage you to read about [other search filters](https://help.github.com/articles/searching-issues/) which will help you write more focused queries.

The labels are loosely grouped by their purpose, but it's not required that every issue have a label from every group or that an issue can't have more than one label from the same group.


#### Type of Issue and Issue State

| Label name | Description |
| --- |  --- |
| `enhancement` |  Feature requests. |
| `bug` |  Confirmed bugs or reports that are very likely to be bugs. |
| `question` |  Questions more than bug reports or feature requests (e.g. how do I do X). |
| `feedback` |  General feedback more than bug reports or feature requests. |
| `help-wanted` | The Zoogie core team would appreciate help from the community in resolving these issues. |
| `beginner` |  Less complex issues which would be good first issues to work on for users who want to contribute to Zoogie. |
| `more-information-needed` | More information needs to be collected about these problems or feature requests (e.g. steps to reproduce). |
| `needs-reproduction` | Likely bugs, but haven't been reliably reproduced. |
| `blocked` |  Issues blocked on other issues. |
| `duplicate` |  Issues which are duplicates of other issues, i.e. they have been reported before. |
| `wontfix` |  The Zoogie core team has decided not to fix these issues for now, either because they're working as intended or for some other reason. |
| `invalid` |  Issues which aren't valid (e.g. user errors). |
| `wrong-repo` | Issues reported on the wrong repository  |

#### Topic Categories

| Label name |  Description |
| --- |  --- |
| `windows` | Related to Zoogie running on Windows. |
| `linux` |  Related to Zoogie running on Linux. |
| `mac` | Related to Zoogie running on macOS. |
| `documentation` |  Related to any type of documentation|
| `performance` |  Related to performance. |
| `security` |  Related to security. |
| `ui` | Related to visual design. ||
| `crash` |  Reports of Zoogie completely crashing. |
| `auto-indent` | Related to auto-indenting text. |
| `encoding` | Related to character encoding. |
| `network` |  Related to network problems or working with remote files (e.g. on network drives). |
| `git` | Related to Git functionality (e.g. problems with gitignore files or with showing the correct file status). |


#### Pull Request Labels

| Label name | Description
| --- | --- |
| `work-in-progress` | Pull requests which are still being worked on, more changes will follow. |
| `needs-review` | Pull requests which need code review, and approval from maintainers or Zoogie core team. |
| `under-review` | Pull requests being reviewed by maintainers or Zoogie core team. |
| `requires-changes` | Pull requests which need to be updated based on review comments and then reviewed again. |
| `needs-testing` | Pull requests which need manual testing. |
