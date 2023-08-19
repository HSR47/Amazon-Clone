import FilterArea from "./FilterArea"
import ProductArea from "./ProductsArea"
import styles from './SearchPage.module.css'

function SearchResult(){
    return (
        <div className={styles.searchResult}>
            <FilterArea/>
            <ProductArea/>
        </div>
    )
}

export default SearchResult