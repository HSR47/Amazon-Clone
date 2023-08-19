import { useEffect, useRef, useState } from 'react'
import LeftHeader from './LeftHeader'
import MiddleHeader from './MiddleHeader'
import RightHeader from './RightHeader'
import styles from './Header.module.css'

function Part1() {
    let [isSticky , setIsSticky] = useState(false)
    let part1Ref = useRef(null)

    useEffect(function(){

        function handleScroll(){
            let part1Height = part1Ref.current.offsetHeight
            if (window.scrollY > part1Height)
                setIsSticky(true)
            else
                setIsSticky(false)
        }

        window.addEventListener('scroll' , handleScroll)
        return function(){
            window.removeEventListener('scroll' , handleScroll)
        }
    } , [])

    return (
        <div ref={part1Ref} className={`${styles.part1} ${isSticky ? `${styles.sticky}` : ''}`}>
            <LeftHeader />
            <MiddleHeader />
            <RightHeader />
        </div>
    )
}

export default Part1