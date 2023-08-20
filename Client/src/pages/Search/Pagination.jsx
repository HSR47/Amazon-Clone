import { useState } from "react"
import styles from './SearchPage.module.css'

let totalPages = 20

function Pagination(){
    let [currentPage , setCurrentPage] = useState(1)

    function handleBtnClick(e){
        let btnEle = e.target.closest('button')
        if (btnEle.dataset.page>=1 && btnEle.dataset.page<=totalPages)
            setCurrentPage(btnEle.dataset.page)
    }

    return (
        <div className={styles.paginationContainer}>
            <div className={styles.pagination}>
                <button onClick={handleBtnClick} className={styles.prev} data-page={Number(currentPage)-1}><img src="/leftPage.svg" data-left/>Previous</button>
                {Number(currentPage)>=3 && <button onClick={handleBtnClick} data-page={1}>1</button>}
                {Number(currentPage)>=4 && <button className={styles.dot}>...</button>}
                {Number(currentPage)>1 && <button onClick={handleBtnClick} data-page={Number(currentPage)-1}>{Number(currentPage)-1}</button>}
                <button data-active data-page={Number(currentPage)}>{Number(currentPage)}</button>
                {Number(currentPage)<totalPages && <button onClick={handleBtnClick} data-page={Number(currentPage)+1}>{Number(currentPage)+1}</button>}
                {Number(currentPage)<totalPages-2 && <button className={styles.dot}>...</button>}
                {Number(currentPage)<=totalPages-2 && <button onClick={handleBtnClick} data-page={totalPages}>{totalPages}</button>}
                <button onClick={handleBtnClick} className={styles.next} data-page={Number(currentPage)+1}>Next<img src="/rightPage.svg" data-right/></button>
            </div>
        </div>
    )
}

export default Pagination