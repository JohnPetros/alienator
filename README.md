<h1 align="center">
  Alienator 👽
</h1>

<div align="center">
   <a href="https://github.com/JohnPetros">
      <img alt="Made by JohnPetros" src="https://img.shields.io/badge/made%20by-JohnPetros-blueviolet">
   </a>
   <img alt="GitHub Language Count" src="https://img.shields.io/github/languages/count/JohnPetros/alienator">
   <a href="https://github.com/JohnPetros/alienator/commits/main">
      <img alt="GitHub Last Commit" src="https://img.shields.io/github/last-commit/JohnPetros/alienator">
   </a>
  </a>
   </a>
   <a href="https://github.com/JohnPetros/alienator/blob/main/LICENSE.md">
      <img alt="GitHub License" src="https://img.shields.io/github/license/JohnPetros/alienator">
   </a>
    <img alt="Stargazers" src="https://img.shields.io/github/stars/JohnPetros/alienator?style=social">
</div>
<br>



## 🖥️ About the project

Alienator is a web game where the user should guess the character name of Alienator, the boss of the game.

The user should send their question to Alienator who answers whether the question is correct or not as well as tips at sometimes to help them. The user has up to 15 attempts to guess it correctly.

The goal of developing this project was learn the features of [HTMX](https://htmx.org/), an amazing web technology that gives you access to AJAX without [JavaScript](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript), as well as [_hyperscript](https://hyperscript.org/), an easy lib to execute JavaScript code directly in HTML (similiar to [Tailwind](https://tailwindcss.com/) but for JS 😜).

### ⏹️ Demonstration

<table align="center">
  <tr>
    <td align="center" width="600" height="300">
    <img src=".github/images/preview.gif" alt="Preview of the application" />
    </td>
  </tr>
</table>

---

## ✨ Features

### User

- [x] The game should be switch between 3 states: *ready to start* and *running*
- [x] The user should start the game by a button if the game is *ready to start*
- [x] The user should send a question to *Alienator* by a form if the game is *running*
- [x] The user should not stop the game if it is *running*, that means the game only ends after the user wins or loses
- [x] The user should start as many games as they want


### Alienator

- [x] *Alienator* should think the name of a character as the game starts
- [x] *Alienator* should avoid giving simple yes or no answers
- [x] *Alienator* should answers user's question but he can never reveal the character he thought of
- [x] *Alienator* should give user some hints in some of his asnwers to help them to guess it correclty
- [x] *Alienator* should congratulate user if they manage to guess the character's name
- [x] *Alienator* should mock the user if the cannot guess the character's name
- [x] *Alienator* should say the name of the character as the game ends regardless whether the user won or lost
- [x] *Alienator* should not answers not friendly family questions
- [x] The *Alienator*'s cat should inform the user how many attempts are left (this number should be updated with each question)
- [x] The "wisdom" of *Alienator* shoud come from an AI

### Game state

- [x] The left attempts and The history of the user and *Alienator* "chat" should be saved while the game is *running*
- [x] The history should empty and the attempts should reset to 15 if the game is *ready to start*
    
### Layout

- [x] The layout and the game behavior should adapt to the user device regardless of its size

---

## ⚙️ Architecture

## 🛠️ Technologies and tools

- **[HTMX](https://tailwindcss.com/)** to make requests to the server directly on the HTML

- **[Hyperscript](https://hyperscript.org/)** to make some components interactive

- **[Python Flask](https://flask.palletsprojects.com/en/3.0.x/)** to build the server

- **[Gemini Ai](https://gemini.google.com/app)** to serve as the "wisdom" of *Alienator*

- **[Tailwind](https://tailwindcss.com/)** to style the app

- **[Flowbite UI](https://preline.co/)** to build static accessible ui components with tailwind


> For more details about the project's dependencies like specific versions of each dependency, see [package.json](https://github.com/JohnPetros/alienator/blob/main/package.json) and [requirements.txt](https://github.com/JohnPetros/alienator/blob/main/requirements.txt)

---

## 🚀 How to run the application?

#### In the hardest way 😔

### 🔧 Prerequisites

Before download the prject you will need install some tools:

- [pip] to install python packages
- [npm](https://nodejs.org/en), [yarn](https://nodejs.org/en) or [pnpm](https://pnpm.io/pt/) (I'll use pnpm) to install node packages

> Besides that, it is good to have some tool to write the code like [VSCode](https://code.visualstudio.com/)

> Also it is pivotal setting the environment variables on the `.env` file before running the application. See the [.env.example](https://github.com/JohnPetros/alienator/blob/main/.env.example) file to know which variables should be set

### 📟 Running the aplication

```bash

# Clone this repo
$ git clone https://github.com/JohnPetros/alienator.git .

# Install the python dependencies
$ pip install -r requirements.txt

# Install the node dependencies
$ pnpm install

# Run the application on a development environment
$ pnpm dev

```

> Probably the aplication will be running on http://localhost:5000

---

#### In the (Docker) easiest way 😄

### 📟 Running the aplication

### 🔧 Prerequisites

- [Docker](https://www.docker.com/) the amazing technology to manage [containers](https://www.docker.com/resources/what-container/).


```bash

# Run
$ docker compose up --build

```

> Probably the aplication will be running on http://localhost:5000

## 🚚 Deploy

This application's deploy was made using **[Rende plataform](https://www.render.com/)**, which means you can use the running application accessing this **[link](https://alienator.onrender.com)**.

---

## 🤝 how to Contribute

```bash

# Fork this repo
$ git clone https://github.com/JohnPetros/alienator.git

# Create a nem branch for the new feature
$ git checkout -b new-feature

# Commit your changes:
$ git commit -m 'feat: <New Feature>'

# Push your branch:
$ git push origin new-feature

```

> You must replace new-feature with the name the feature you are adding

> You can also open a [new issue](https://github.com/JohnPetros/alienator/issues) about some problem, question or sugestion for the project. I will be happy to help as well as improve this application

---

## 📝 Licence

This application is under MIT Licence. See [the licence file](https://github.com/JohnPetros/alienator/blob/main/license) to get more details about it.

---

<p align="center">
  Made with 💜 by John Petros 👋🏻
</p>
