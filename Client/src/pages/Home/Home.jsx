import Carousel from "./Carousel"
import styles from './Home.module.css'

function Home()
{
    return (
        <div className={styles.home}>
            <Carousel/>
        </div>
    )
}

export default Home