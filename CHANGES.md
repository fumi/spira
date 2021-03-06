# Changelog for Spira <http://github.com/datagraph/spira>

## untagged
 * Small updates for RDF.rb 0.2.0 compatibility
 * Add a Spira::Base class that can be inherited from for users who prefer to
   inherit rather than include.
 * Resource#new returns to the public API as a way to create a resource with a
   new blank node subject.

## 0.0.3
 * Bumped promise dependency to 0.1.1 to fix a Ruby 1.9 warning
 * Rework error handling when a repository is not configured; this should
   always now raise a Spira::NoRepositoryError regardless of what operation 
   was attempted, and the error message was improved as well.
 * A '/' is no longer appended to base URIs ending with a '#'
 * Resources can now take a BNode as a subject.  Implemented #node?, #uri,
   #to_uri, #to_node, and #to_subject in support of this; see the yardocs for
   exact semantics.  RDF::Node is monkey patched with #as, just like RDF::URI,
   for instantiation.   Old code should not break, but if you want to add
   BNodes, you may be using #uri where you want to now be using #subject.

## 0.0.2
 * Implemented #each on resource classes, allowing classes with a defined RDF
   type to be enumerated
 * Fragment URIs are now used as strings, allowing i.e. Integers to be used as
   the final portion of a URI for classes with a base_uri defined.
 * Added an RDF::URI property type
 * Implemented #to_rdf and #to_uri for increased compatibility with the RDF.rb 
   ecosystem

## 0.0.1
 * Initial release
