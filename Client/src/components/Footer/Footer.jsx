
import styles from './Footer.module.css'

function Footer()
{
    let details = [
        { heading : "Get to Know Us" , links : ['About Us' , 'Careers' , 'Press Release' , 'Amazon Science']},
        { heading : "Connect with Us" , links : ['Facebook' , 'Twitter' , 'Instagram']},
        { heading : "Make Money with Us" , links : ['Sell on Amazon' , 'Sell under Amazon Accelarator' , 'Protect and Build Your Brand' , 'Amazon Global Selling' , 'Become an Affiliate' , 'Fulfilment by Amazon' , 'Advertise Your Products' , 'Amazon Pay on Merchants']},
        { heading : "Let us Help You" , links : ['COVID-19 and Amazon' , 'Your Account' , 'Returns Centre' , '100% Purchase Protection' , 'Amazon App Download' , 'Help']},

    ]

    return (
        <div className={styles.footer}>
            <button className={styles.backToTop}>
                <p>Back to top</p>
            </button>

            <div className={styles.details}>
                {details.map(function(i){
                    return (
                        <div key={i.heading}>
                            <h1>{i.heading}</h1>
                            <div className={styles.links}>
                                {i.links.map(function(j){
                                    return <p key={j}>{j}</p>
                                })}
                            </div>
                        </div>
                    )
                })}
            </div>

            <div className={styles.logo}>
                <img src="/logo.png" alt="logo" />
            </div>
        </div>
    )
}

export default Footer