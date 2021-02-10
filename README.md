
# Desafio: Programa de Formação em Elixir

Solution of the [challenge proposed](https://gist.github.com/programa-elixir/1bd50a6d97909f2daa5809c7bb5b9a8a) by [Stone](https://www.stone.com.br/) for the Elixir Training Program

## Getting Started

Instructions for preparing and using the developed app.

### Prerequisites

What you need install to make it work:

* Python 3.7.x or newer
* Pandas Library by using pip install pandas

This application takes its inputs from CSV files that must have the following structure:

#### shopping_list.csv:

```

 NAME;QUANTITY;PRICE
 itemA;integer;integer
 itemB;integer;integer
 itemC;integer;integer
 .
 .
 .

```

* NAME: Column of items names 
* QUANTITY: Column of items quantities 
* PRICE: Column of items unit prices (in cents)

#### email_list.csv:

```

 CLIENT
 a@email.com
 b@email.com
 c@email.com
 .
 .
 .

```

* CLIENT: Column of emails of a purchase order

**Both files must have the header as demonstrated**

### Usage

At your terminal:

```

 git clone https://github.com/Wuerike/desafio-elixir-stone
 cd /path/to/desafio-elixir-stone
 python app.py

```

## Autor

* **Wuerike Cavalheiro** - [GitHub](https://github.com/Wuerike)
