---
theme : "moon"
transition: "slide"
highlightTheme: "atom-one-dark"
logoImg: "images/logo.png"
slideNumber: false
title: "Dev Life w/ VSCode Dev Containers"
---

## Dev Life w/ VSCode Dev Containers

<!-- .slide: data-background="linear-gradient(rgba(0, 0, 0, 0.85), rgba(0, 0, 0, 0.65)), url(images/background-rect.jpeg)" -->

Christopher Bailey <br><br>
Thanks to Nick Muoh for Template {style=color:#A0A603;background:#0D0D0D}

---

## Agenda

1. Intro
2. The What and Why
3. Getting started w/ Dev Containers
4. Demo
5. Lessons Learned

---

<!-- Intro -->

![](images/logo.png) {align=left style=width:400px;position:absolute}

:::{align=right}
<br><br>

Christopher Bailey

*Site Reliability Engineer @[Multi Media]([http://](https://multimediallc.com/))*  {style=color:#A0A603;background:#0D0D0D;width:400px;padding:10px}

<br>

--

<!--
Talk about yourself here:
 - Where you work?
 - What you do?
 - Anything else you want the audience to know about you.
-->

- Work for a company that does live streaming.
  - Main monolith is Django/Python
- Primary job is all pre-production environments.
  - CI/Testing, Github Actions, Docker, etc.
- Been doing Python since 2014.
- Was at American Greetings for 5 years.

---

## What are Dev Containers

<!--
First talk about what containers are at a high level. Here is
quick blurb about that
-->

> [Containers](https://www.docker.com/resources/what-container) are pieces of software that package code and all of the dependencies that code needs to run, including the runtime, tools, libraries, and settings.

--

### Images and Containers

> When you create a container, its initial contents come from what's known as an **image**. An image can be thought of as a mini-disk drive with things like the operating system and other tools pre-installed.
>
> You describe what goes into the image using a Dockerfile, and once you run the image, it becomes a container.

--

<!--
While I do not want this to turn into a Docker talk, understanding some high level concepts of Docker will really help understand the technology and how it works. Especially with how confusing the container world can be.
-->

### Docker and OCI

> "Container" is a generic term for any Open Container Initiative (OCI) compatible container. OCI images can be ran by any OCI orchestrator ([Docker](https://www.docker.com/), [Podman](https://podman.io/), [Kubernetes](https://kubernetes.io/), etc.)
>
> Docker is the most popular orchestrator since they are the originally company that came out with containers.

--

<!-- .slide: data-fullscreen -->

### Docker Desktop vs. Docker Engine

- Containers sandbox a file system within your OS
- Allow you to multiple copies of your OS at once
- While very similar to VMs in concept, **they do not use virtualization**
- Host OS must use the same kernel as your container
  - Docker Engine is the OCI orchestrator
  - Docker Desktop is a GUI around a VM + Docker Engine.
- Performance:
  - Native > Engine (Linux) > WSL2+Desktop > Desktop > VM

<!--
I do not have any hard stats to back up the performance order, but it is purely anecdotal from our devs trying to use Docker on our monolith at work.

Notes (may not cover everything):

Docker on Linux uses cgroups and gives near native performance. The only real overhead is the virtualized network adapters.

Microsoft put nearly 10 years of work into WSL and Docker on Windows which is why WSL2 (VM running inside of HyperV) is so tightly coupled to the OS and in general more performant then traditional VMs.

Docker Desktop + MacOS vs. VM is actually a wash. Since Docker Desktop uses QEMU on MacOS, they are essentially the same and you _might_ actually get worse performance from Docker Desktop on MacOS due to the networking and storage overhead (bind mounts from host to container have to be mounted across the virtual network adapter into the VM).

If you are accepting a job at location that you know uses containers/docker for development, I greatly recommend (in terms of performance, leaving personal performances aside):

    Linux (any distro) > Windows 10/11 (with WSL2) > MacOS > Windows (without WSL2)

Ask how other devs run Docker and if they use Windows 10/11, ask if they are using WSL as Windows without WSL is painful.
-->

--

<!--
Here is a diagram to help you with your explanation
-->

![](https://code.visualstudio.com/assets/blogs/2020/07/27/1-containers-abc.png){align=center style=width:600px}

---

## Why Dev Containers

<!--
This is a great point to talk about why YOU use dev containers
and how it has changed programming for you.
-->

> Dev containers provide a reusable, automated and consistent developer environment saying countless hours and time during setup/onboarding.

--

<!--
Here are some other points for using dev containers.
Taken from this dev.to blog
https://dev.to/mcastellin/hands-on-with-vscode-dev-containers-33bf
-->

There are several advantages of using dev containers... {align=left}

- **Compatibility**: Your code runs in the exact same environment from your development machine all the way to production

- **Automation & Speed**: The creation of a new dev environment is fully automated. You can restore a broken environment (or onboard a new developer) in seconds

--

- **PR Review**: You can check out the code from a PR in a new, isolated container without messing with your work

- **It's CLEAN!** I have tons of small projects on my laptop that I can't even find anymore. With dev containers I could: checkout a project -> build a dev container -> develop and commit my changes -> destroy it immediately

---

## Getting Started

<!--
Here talk about some of the things one
will need to know or be comfortable with to start using dev containers
and be effective. Here is an example
-->

Some things you'll need to know

- Basic knowledge of software development, such as what it means to run code and install a new language

- Containers and basic knowledge using Docker (familiarity with the concept of images, containers, and registries). Great resource for [learning Docker/Containers](https://www.amazon.com/Docker-Shipping-Reliable-Containers-Production/dp/1492036730)

- Git and basic knowledge of GitHub, such as what a repository is

--

### Prerequisites

<!--
Add whatever you think is missing here
-->

- [Visual Studio Code](https://code.visualstudio.com/)
- Docker
  - For Windows: [WSL2](https://docs.microsoft.com/en-us/windows/wsl/) and [Docker Desktop](https://docs.docker.com/desktop/windows/install/)
  - For MacOS: [Docker Desktop](https://docs.docker.com/desktop/mac/install/)
  - For Linux: [Docker Engine](https://docs.docker.com/engine/install/)
- [VS Code's "Remote Development" extension pack](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack)

---

## Demo Time

![](https://media.giphy.com/media/u2pmTWUi0MXjyrMaVj/giphy.gif)

--

<!-- Plan here is to make two demo projects inside of single Github repo (maybe with this presentation too).

    1: (from scratch + Dockerfile)
    * How to check Docker (Desktop + CLI)
    * Install VS Code + Remote Development extension
    * Open "hello world" Python project
    * Add devcontainer.json to project
    * Show command palette

    2: (Docker Compose + fully configured)
    * Open project that uses Docker Compose with preexisting devcontainer.json config (Django + Postgres?)
    * Show "Reopen in Container" option

<!--
Here is where the fun part begins.
You can choose a new simple project to showcase
how to set up dev containers OR choose a project you have already
worked on but set up a dev container for it from scratch!!
-->

Here are a few things that would be great to see.. {align=left}

- Checking to see docker daemon is running
- Installing Remote container extension
- How to add a dev container to an existing project?
  - Talk about the devcontainer.json

--

- How to run a project with a dev container set up?
  - Forwarding ports
  - Creating shortcuts to easily run your project
- Customizing project and editor settings in dev containers (based on your experience)
- How to add additional software to the base image?

---

## Lessons Learned

<!--
Here it would be nice if you could share some
of the lessons you learnt while using dev containers.

* What are some of the things you had issue wrapping your head around
* What are some cool tips and tricks you learnt
-->

---

## The END

*Thanks*
