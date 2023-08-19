
import styles from './Header.module.css'
import Part2 from './Part2'
import Part1 from './Part1'

function Header() {

    return (
        <>
            <div className={styles.header}>
                <Part1/>
                <Part2/>
            </div>
        </>
    )
}

export default Header