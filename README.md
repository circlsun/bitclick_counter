# Bitly url shorterer

This project interacts with the [bit.ly](https://bitly.com/) for trimming links. Your link is sent to the input, and a shortened link like bit.ly/****** is output.
You can also submit an already shortened link to the input, then the output will have the number of clicks on this link. 

Entering and receiving a shortened link is carried out in the terminal

## Usage

Just run the python script `main.py` with the following concole command:
```
python main.py <your URL>
```
For example:
```
python main.py https://dvmn.org/
```
The result will be:
```
Битлинк: bit.ly/3VtdK6W
Число кликов по ссылке: 0
```

## Installation

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```
I don't think you need to use any virtual envs for such a small script.

## Project Goals

The code is written for educational purposes for the online-course of the Web Services API on [Devmen](https://dvmn.org/)
