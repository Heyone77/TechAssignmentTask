from typing import Optional, List

from pydantic import BaseModel, HttpUrl, field_validator


class ArtObject(BaseModel):
    objectID: int
    isHighlight: Optional[bool] = None
    accessionNumber: Optional[str] = None
    accessionYear: Optional[str] = None
    isPublicDomain: Optional[bool] = None
    primaryImage: Optional[HttpUrl] = None
    primaryImageSmall: Optional[HttpUrl] = None
    additionalImages: Optional[List[HttpUrl]] = None
    constituents: Optional[List[dict]] = None
    department: Optional[str] = None
    objectName: Optional[str] = None
    title: Optional[str] = None
    culture: Optional[str] = None
    period: Optional[str] = None
    dynasty: Optional[str] = None
    reign: Optional[str] = None
    portfolio: Optional[str] = None
    artistRole: Optional[str] = None
    artistPrefix: Optional[str] = None
    artistDisplayName: Optional[str] = None
    artistDisplayBio: Optional[str] = None
    artistSuffix: Optional[str] = None
    artistAlphaSort: Optional[str] = None
    artistNationality: Optional[str] = None
    artistBeginDate: Optional[str] = None
    artistEndDate: Optional[str] = None
    artistGender: Optional[str] = None
    artistWikidata_URL: Optional[HttpUrl] = None
    artistULAN_URL: Optional[HttpUrl] = None
    objectDate: Optional[str] = None
    objectBeginDate: Optional[int] = None
    objectEndDate: Optional[int] = None
    medium: Optional[str] = None
    dimensions: Optional[str] = None
    measurements: Optional[List[dict]] = None
    creditLine: Optional[str] = None
    geographyType: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    county: Optional[str] = None
    country: Optional[str] = None
    region: Optional[str] = None
    subregion: Optional[str] = None
    locale: Optional[str] = None
    locus: Optional[str] = None
    excavation: Optional[str] = None
    river: Optional[str] = None
    classification: Optional[str] = None
    rightsAndReproduction: Optional[str] = None
    linkResource: Optional[HttpUrl] = None
    metadataDate: Optional[str] = None
    repository: Optional[str] = None
    objectURL: Optional[HttpUrl] = None
    tags: Optional[List[dict]] = None
    objectWikidata_URL: Optional[HttpUrl] = None
    isTimelineWork: Optional[bool] = None
    GalleryNumber: Optional[str] = None

    @field_validator('primaryImage', 'primaryImageSmall', 'artistWikidata_URL', 'artistULAN_URL', 'linkResource',
                     'objectURL', 'objectWikidata_URL', mode='before')
    @classmethod
    def check_image_url(cls, v):
        if v == '':
            return None
        return v


class ArtObjectList(BaseModel):
    total: int
    objectIDs: List[int]
