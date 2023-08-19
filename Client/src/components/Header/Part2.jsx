import styles from './Header.module.css'

function Part2(){
    return (
        <div className={styles.part2}>
            <button className="home">Home</button>
            <button className="ourStore">Our Store</button>
            <button className="contact">Contact</button>
            <button className="blogs">Blogs</button>
        </div>
    )
}

export default Part2