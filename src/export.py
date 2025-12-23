"""
Data export utilities for multiple formats
"""

import json
import logging
from typing import List, Dict, Any
from io import BytesIO, StringIO

logger = logging.getLogger("DataExporter")


class DataExporter:
    """Export data in various formats"""
    
    @staticmethod
    def export_to_csv(data: List[Dict[str, Any]]) -> str:
        """Export data to CSV format"""
        try:
            import pandas as pd
            
            if not data:
                return ""
            
            df = pd.DataFrame(data)
            csv_string = df.to_csv(index=False)
            logger.info(f"✓ Exported {len(data)} rows to CSV")
            return csv_string
            
        except ImportError:
            logger.error("pandas not installed. Install with: pip install pandas")
            raise
        except Exception as e:
            logger.error(f"CSV export failed: {str(e)}")
            raise
    
    @staticmethod
    def export_to_excel(data: List[Dict[str, Any]]) -> bytes:
        """Export data to Excel format"""
        try:
            import pandas as pd
            
            if not data:
                return b""
            
            df = pd.DataFrame(data)
            
            # Create Excel file in memory
            output = BytesIO()
            with pd.ExcelWriter(output, engine='openpyxl') as writer:
                df.to_excel(writer, index=False, sheet_name='Data')
            
            excel_bytes = output.getvalue()
            logger.info(f"✓ Exported {len(data)} rows to Excel")
            return excel_bytes
            
        except ImportError:
            logger.error("pandas or openpyxl not installed. Install with: pip install pandas openpyxl")
            raise
        except Exception as e:
            logger.error(f"Excel export failed: {str(e)}")
            raise
    
    @staticmethod
    def clean_data(data: List[Dict[str, Any]], 
                   remove_duplicates: bool = False,
                   remove_nulls: bool = False) -> List[Dict[str, Any]]:
        """Clean and process data"""
        cleaned = data.copy()
        
        # Remove duplicates
        if remove_duplicates:
            seen = set()
            unique_data = []
            for item in cleaned:
                item_str = json.dumps(item, sort_keys=True)
                if item_str not in seen:
                    seen.add(item_str)
                    unique_data.append(item)
            cleaned = unique_data
            logger.info(f"✓ Removed {len(data) - len(cleaned)} duplicates")
        
        # Remove null values
        if remove_nulls:
            cleaned = [
                {k: v for k, v in item.items() if v is not None and v != ''}
                for item in cleaned
            ]
            logger.info("✓ Removed null values")
        
        return cleaned
    
    @staticmethod
    def transform_data(data: List[Dict[str, Any]], 
                      transformations: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Apply transformations to data"""
        
        # Example transformations:
        # - lowercase_fields: ["name", "email"]
        # - uppercase_fields: ["country"]
        # - trim_fields: ["description"]
        # - extract_domain_from: "email"
        
        transformed = []
        
        for item in data:
            new_item = item.copy()
            
            # Lowercase fields
            for field in transformations.get("lowercase_fields", []):
                if field in new_item and isinstance(new_item[field], str):
                    new_item[field] = new_item[field].lower()
            
            # Uppercase fields
            for field in transformations.get("uppercase_fields", []):
                if field in new_item and isinstance(new_item[field], str):
                    new_item[field] = new_item[field].upper()
            
            # Trim fields
            for field in transformations.get("trim_fields", []):
                if field in new_item and isinstance(new_item[field], str):
                    new_item[field] = new_item[field].strip()
            
            transformed.append(new_item)
        
        logger.info(f"✓ Applied transformations to {len(data)} items")
        return transformed
