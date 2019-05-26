# ShelpinETHMAD

Objective is showing how a card transaction generates a token refund that represents a 1:1 debt of the seller with an NGO of customer choice.

In this PoC, the order success event triggers a transaction from an account where tokens were preminted to the customer wallet.

Purchase success events are captured in a chrome extension to transfer tokens with a plugin implementation in the  e-commerce site used for the PoC. 

Login is made with Django for users, merchants and ngo´s. Merchants provide the % donation that they are willing to donate. 

For the test e-commerce we setup a woocommerce store in which the plugin that generates the transactions is installed, and a stripe test account waas set up to make the card payment transaction. 







