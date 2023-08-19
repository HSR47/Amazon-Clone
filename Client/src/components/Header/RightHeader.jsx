import styles from './Header.module.css'

function RightHeader(){
    return (
        <div className={styles.right}>

            <button className={styles.account}>
                <p className={styles.greet}>Hello, Himanshu</p>
                <p lassName={styles.acc}>Account <img src="/white-dropdown.svg" alt="dropdown" /></p>
            </button>


            <button className={styles.wishlist}>
                <p className={styles.first}>Your</p>
                <p className={styles.secong}>Wishlist <img src="/wishlist.svg" alt="wishlist" /></p>
            </button>


            <button className={styles.cart}>
                <span>1</span>
                <img src="/cart.svg" alt="cart" />
                <p>Cart</p>
            </button>
        </div>
    )
}

export default RightHeader