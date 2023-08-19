import { useEffect, useState } from 'react'
import styles from './SearchPage.module.css'

let sortByMapping = {
    plth : "Price: Low to High",
    phtl : "Price: High to Low",
    act : "Avg. Customer Reviews",
    na : "Newest Arrivals"
}

let sortByOptions = []

for (let i in sortByMapping)
{
    sortByOptions.push(
        {
            title : sortByMapping[i],
            value : i
        }
    )
}

function SearchInfo(){
    let [sortBy , setSortBy] = useState('plth')
    let [isSortByUlActive , setIsSortByUlActive] = useState(false)

    function handleSortByClick(e){
        setIsSortByUlActive(true)
    }

    function handleOptionClick(e){
        let liEle = e.target.closest('li')
        setSortBy(liEle.dataset.value)
        setIsSortByUlActive(false)
    }

    useEffect(function(){
        function closeSortBy(e){
            if (!e.target.closest('#sortByUl') && !e.target.closest('#sortByBtn'))
                setIsSortByUlActive(false)
        }

        window.addEventListener('click' , closeSortBy)
        return function(){
            window.removeEventListener('click' , closeSortBy)
        }
    } , [])

    return (
        <div className={styles.searchInfoContainer}>
            <div className={styles.searchInfo}>
                <p>1-24 of 220 results</p>
                <div className={styles.sortBy}>
                    <button id='sortByBtn' onClick={handleSortByClick}>Sort by : {sortByMapping[sortBy]} <img src="/dropdown.svg"/></button>
                    <ul id='sortByUl' style={{display : isSortByUlActive ? 'flex' : 'none'}} className={styles.options}>
                        {sortByOptions.map(function(i , ind){
                            return (
                                <li onClick={handleOptionClick} key={ind} data-value={i.value} data-active={sortBy==i.value ? 'true' : 'false'}>{i.title}</li>
                            )
                        })}
                    </ul>
                </div>
            </div>
        </div>
    )
}

export default SearchInfo