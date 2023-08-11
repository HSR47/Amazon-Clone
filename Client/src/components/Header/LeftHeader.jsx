import styles from './styles/Header.module.css'


function LeftHeader(){
    return (
        <div className={styles.left}>

            
            <button className={styles.logo}>
                <img src="/logo.png" alt="Logo" />
                <p>.in</p>
            </button>
            
            
            <button className={styles.address}>
                <p>Address</p>
            </button>
        </div>
    )
}

export default LeftHeader