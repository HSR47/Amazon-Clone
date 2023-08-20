import ReactStars from 'react-stars'
import styles from './SearchPage.module.css'


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

function getDeliveryDate(){
    let currentDate = new Date();
    
    let maxDaysToAdd = 6
    let minDaysToAdd = 3
    let daysToAdd = Math.floor(Math.random() * (maxDaysToAdd - minDaysToAdd + 1) + minDaysToAdd)
    
    let deliveryDate = new Date(currentDate)
    deliveryDate.setDate(deliveryDate.getDate() + daysToAdd)

    return deliveryDate
}

let  dayNames = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
const monthNames = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];

function ProductRow({ info }) {
    let delivery = getDeliveryDate()
    let deliveryDay = dayNames[delivery.getDay()]
    let deliveryDate = delivery.getDate()
    let deliveryMonth = monthNames[delivery.getMonth()]

    return (
        <div className={styles.productRow}>
            <div className={styles.imgContainer}>
                <img src={info.img} onClick={function(){console.log("lul")}}/> 
            </div>
            <div className={styles.details}>
                <p className={styles.title}>{info.title}</p>
                <div className={styles.rating}>
                    <div className={styles.value}>{info.stars}</div>
                    <div className={styles.stars} data-value={roundStars(info.stars)}></div>
                    <div className={styles.total}>68</div>
                </div>
                <div className={styles.price}><span>₹</span>{info.price.toLocaleString()}</div>
                <div className={styles.deliveryIn}>
                    <p className={styles.getItBy}>Get it by <span>{deliveryDay}, {deliveryDate} {deliveryMonth}</span></p>
                    <p className={styles.free}>FREE Delivery by Amazon</p>
                </div>
            </div>
        </div>
    )
}

export default ProductRow