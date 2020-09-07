This is a mermaid diagram, you may need to install a [Browser Plugin](https://github.com/BackMarket/github-mermaid-extension) or [VsCode extension](https://marketplace.visualstudio.com/items?itemName=bierner.markdown-mermaid) or similar to view it.

You can also [view it full screen as an SVG](https://mermaid.ink/svg/c2VxdWVuY2VEaWFncmFtCiAgc3RhcnQtPj5Xb3JsZC53b3JsZDogY2FsbHMgeDEKICBXb3JsZC53b3JsZC0+PldvcmxkLl93OiBjYWxscyB4MQogIFdvcmxkLl93LS0+PldvcmxkLndvcmxkOiByZXR1cm5zIHN0cgogIFdvcmxkLndvcmxkLT4+V29ybGQuX286IGNhbGxzIHgxCiAgV29ybGQuX28tLT4+V29ybGQud29ybGQ6IHJldHVybnMgc3RyCiAgV29ybGQud29ybGQtPj5Xb3JsZC5fcjogY2FsbHMgeDEKICBXb3JsZC5fci0tPj5Xb3JsZC53b3JsZDogcmV0dXJucyBzdHIKICBXb3JsZC53b3JsZC0+PldvcmxkLl9sOiBjYWxscyB4MQogIFdvcmxkLl9sLS0+PldvcmxkLndvcmxkOiByZXR1cm5zIHN0cgogIFdvcmxkLndvcmxkLT4+V29ybGQuX2Q6IGNhbGxzIHgxCiAgV29ybGQuX2QtLT4+V29ybGQud29ybGQ6IHJldHVybnMgc3RyCiAgV29ybGQud29ybGQtLT4+c3RhcnQ6IHJldHVybnMgc3RyCg==)        

```mermaid
sequenceDiagram
  start->>World.world: calls x1
  World.world->>World._w: calls x1
  World._w-->>World.world: returns str
  World.world->>World._o: calls x1
  World._o-->>World.world: returns str
  World.world->>World._r: calls x1
  World._r-->>World.world: returns str
  World.world->>World._l: calls x1
  World._l-->>World.world: returns str
  World.world->>World._d: calls x1
  World._d-->>World.world: returns str
  World.world-->>start: returns str

```
