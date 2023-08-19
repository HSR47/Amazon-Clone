import { useParams } from "react-router-dom"
import SearchInfo from "./SearchInfo"
import SearchResult from "./SearchResult"
import Pagination from "./Pagination"
import styles from "./SearchPage.module.css"

function SearchPage(){
    let {slug} = useParams()

    return (
        <div className={styles.searchPage}>
            <SearchInfo/>
            <SearchResult/>
            <Pagination/>
        </div>
    )
}

export default SearchPage