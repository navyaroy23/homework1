select lf.listing_id as Listing_ID, lf.latitude as Latitude, lf.longitude as Longituse, lf.price as Price_2018, pp.price as Price_2017,Anh.price as Price_2019
FROM listing_file lf
inner join price_prediction pp
on lf.listing_id = pp.listing_id
inner join airbnb_nyc_homes anh
on Anh.listing_id = lf.listing_id
