# Reflection: Mock Objects, XP Testing Layers and Serendipitous Decoupling

## 1. How did writing an isolated test force you to improve the design of SaveManager?

When I tested `SaveManager` in Phase 2, I had to use `@patch("persistence.sqlite3.connect")`, which meant the test depended on how the class was implemented internally. This showed me that `SaveManager` was too tightly coupled to the database, which made it difficult to isolate for testing. In Phase 4 I could simply pass a `Mock()` in as a dependency with `SaveManager(Mock())`, without using patch at all. This showed that the difficulty of writing the test had actually been a signal of a problem in the design of the class.

## 2. Why is a unit test with mocks more efficient for this scenario than a full integration test?

A unit test with a mock is faster and easier to control, because it does not need a real database, tables, or cleaning up data after each test. My three tests ran in a fraction of a second because they only worked with mock objects. I could also easily test what happens when the database is down by using `side_effect`, instead of actually stopping a database. This makes the unit test well suited to checking the behaviour of `SaveManager` in isolation. However, integration tests are still needed at a higher level of the testing pyramid, because a mock only checks that my code calls the database correctly, not that the SQL itself works against a real table.

## 3. How does removing the design smell of Fragility help the team respond to changing requirements?

After Phase 4, `SaveManager` does not need to know whether data is saved to SQLite or through an API, because the dependency can be swapped. When the API is ready, we only need to implement the `ApiSaver` class, while `SaveManager` and its tests do not have to be rewritten. This follows the Open-Closed Principle, because we can add new behaviour without changing code that already works. As a result, the team can react to new requirements more easily, instead of following the original plan regardless of the changes.