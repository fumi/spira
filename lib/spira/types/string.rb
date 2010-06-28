module Spira::Types

  ##
  # A {Spira::Type} for string values.  Values will be associated with the
  # `XSD.string` type
  #
  # A {Spira::Resource} property can reference this type as
  # `Spira::Types::String`, `String`, or `XSD.string`.
  #
  # @see Spira::Type
  # @see http://rdf.rubyforge.org/RDF/Literal.html
  class String

    include Spira::Type

    def self.unserialize(value)
      if value.has_language?
        sprintf('"%s"@%s', value.object.to_s, value.language)
      else
        value.object.to_s
      end
    end

    def self.serialize(value)
      s = value.to_s
      if /^"(.+)"@([A-Za-z]{2})$/.match(s)
        RDF::Literal.new($1, :language => $2)
      else
        RDF::Literal.new(s)
      end
    end

    register_alias XSD.string

  end
end
