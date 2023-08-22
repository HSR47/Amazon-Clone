
import styles from './ProductPage.module.css'

function roundStars(star){
    if (star > 4.5)
        return 5

    if (star>4 && star<=4.5)
        return 4.5
    
    if (star>3.5 && star<=4)
        return 4

    if (star>3 && star<=3.5)
        return 3.5

    if (star>2.5 && star<=3)
        return 3
    
    if (star>2 && star<=2.5)
        return 2.5
    
    if (star>1.5 && star<=2)
        return 2
    
    if (star>1 && star<=1.5)
        return 1.5

    if (star>0.5 && star<=1)
        return 1
    
    if (star>0 && star<=0.5)
        return 0.5
}

function Details({product}){
    return (
        <div className={styles.details}>
            <div className={styles.title}>{product.title}</div>

            <div className={styles.brand}>Brand : {product.brand}</div>

            <div className={styles.rating}>
                <p>{product.stars}</p>
                <div id='stars' data-value={roundStars(product.stars)}></div>
                <p>{product.totalRatings} Ratings</p>
            </div>

            <div className={styles.price}><span>₹</span>{product.price.toLocaleString()}</div>

            <div id='fulfilled'>
                <div id="container">
                    <div id='icon'></div>
                    <div id='text'>Fulfilled</div>
                </div>
            </div>

            <div className={styles.emi}>
                <p>Inclusive of all taxes</p>
                <p><span>EMI</span> starts at ₹1,469. No Cost EMI available</p>
            </div>

            <div className={styles.offers}>
                <div className={styles.container}>
                    <div className={styles.icon}>
                        <img src="https://m.media-amazon.com/images/G/31/A2I_CEPC/VSX/vsx_sprite_2x.png"/>
                    </div>
                    <h1>Offers</h1>
                </div>
                <ul>
                    <li>
                        <div>Bank Offer</div>
                        <p>Upto ₹2,000.00 discount on select Credit Cards, HDF…</p>
                    </li>
                    <li>
                        <div>No Cost EMI</div>
                        <p>Upto ₹1,620.60 EMI interest savings on Amazon Pay…</p>
                    </li>
                    <li>
                        <div>Partner Offers</div>
                        <p>Get One Mini Skill Course for FREE on purchase of Lapto…</p>
                    </li>
                </ul>
            </div>

            <div className={styles.features}>
                <div>
                    <img src="https://m.media-amazon.com/images/G/31/A2I-Convert/mobile/IconFarm/icon-returns._CB484059092_.png"/>
                    <p>7 days Replacement by Brand</p>
                </div>
                <div>
                    <img src="https://m.media-amazon.com/images/G/31/A2I-Convert/mobile/IconFarm/trust_icon_free_shipping_81px._CB630870460_.png"/>
                    <p>Free Delivery</p>
                </div>
                <div>
                    <img src="https://m.media-amazon.com/images/G/31/A2I-Convert/mobile/IconFarm/icon-top-brand._CB617044271_.png"/>
                    <p>Top Brand</p>
                </div>
                <div>
                    <img src="https://m.media-amazon.com/images/G/31/A2I-Convert/mobile/IconFarm/icon-amazon-delivered._CB485933725_.png"/>
                    <p>Amazon Delivered</p>
                </div>
            </div>

            <div className={styles.desc}>
                <h1>About this item</h1>
                <p>{product.description}</p>
            </div>
        </div>
    )
}

export default Details