- [1. Goal](#1-goal)
- [2. What is `uv`](#2-what-is-uv)
- [3. Why `uv`?](#3-why-uv)
- [4. Guide to understand `uv`](#4-guide-to-understand-uv)
  - [4.1. Choosing the installation method](#41-choosing-the-installation-method)
  - [4.2. Read what can `uv` do](#42-read-what-can-uv-do)
  - [4.3. Understand Python project](#43-understand-python-project)

# 1. Goal
We will learn how to manage Python

# 2. What is `uv`

> [`uv`](https://docs.astral.sh/uv/): An extremely fast Python package and project manager, written in Rust.

You can read more about it in the [documentation](https://docs.astral.sh/uv/).

Now I will explain why in my own words.

# 3. Why `uv`?

Before we answer this question, we have to understand what a `Python project` is.

Look at this [pandas github](https://github.com/pandas-dev/pandas) as an example.

It is a lot, and you probably don't know where the source code of the `Pandas` is.
But that is because you don't know the "Standard Practice" of a Python project.
If we use a project management tool like `uv`, it helps us to be in a certain standard practice.

There are many Python project management tools; it just happens that I like `uv`. 
I encourage you to try others and decide for yourself which one you like the best.

# 4. Guide to understand `uv`

*At first, I try to summarize `uv` here. However, I learnt that soon this document will be obsolete. Therefore, I should guide you how to approach `uv`*

## 4.1. Choosing the installation method

To start, you need to have `uv` in your system.
Choose one method that suited your need from [here](https://docs.astral.sh/uv/getting-started/installation).

## 4.2. Read what can `uv` do

[Here](https://docs.astral.sh/uv/getting-started/features/) is what can `uv` do.

Eventhough you don't understand everything, but at least you should be familiar with what it can do.

## 4.3. Understand Python project

Read [this](https://docs.astral.sh/uv/concepts/projects/init/#target-directory).

