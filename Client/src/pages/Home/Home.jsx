import Carousel from "./Carousel"
import Category from "./Category"
import styles from './Home.module.css'

function Home()
{
    return (
        <div className={styles.home}>
            <Carousel/>
            <Category/>
        </div>
    )
}

export default Home